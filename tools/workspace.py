import shutil
from pathlib import Path
import difflib

PORTFOLIO_DIR = Path("portfolio")
WORKSPACE_ROOT = Path(".workspaces")

SECRET_PATTERNS = (".env", ".key", ".pem", "id_rsa", "credentials", "secrets")

def _is_secret(name: str) -> bool:
    low = name.lower()
    return any(p in low for p in SECRET_PATTERNS)

def create_workspace(run_id: str) -> Path:
    '''Crea una copia AISLADA de portfolio/ para esta ejecucion.'''
    WORKSPACE_ROOT.mkdir(exist_ok=True)
    ws = WORKSPACE_ROOT / run_id
    if ws.exists():
        shutil.rmtree(ws)              
    def ignore(_carpeta, nombres):
        return [n for n in nombres if _is_secret(n)]
    shutil.copytree(PORTFOLIO_DIR, ws, ignore=ignore)
    return ws

def read_file(ws: Path, rel: str) -> str:
    return (ws / rel).read_text(encoding="utf-8")


def make_diff(ws: Path, rel: str) -> str:
    '''
        Diff unificado de un archivo entre main (portfolio/) y el workspace.

        Compara el original contra la propuesta y devuelve solo las diferencias,
        en el mismo formato que 'git diff'.
    '''
    main_path= PORTFOLIO_DIR / rel
    old= main_path.read_text(encoding="utf-8").splitlines(keepends=True) if main_path.exists() else []
    new= (ws / rel).read_text(encoding="utf-8").splitlines(keepends=True)

    diff= difflib.unified_diff(
        old, new,
        fromfile=f"main/{rel}",         
        tofile=f"workspace/{rel}",      
    )
    return "".join(diff) or "(sin cambios)"

def write_file(ws: Path, rel: str, content: str) -> None:
    '''Escribe SOLO dentro del workspace (jamas en portfolio/).'''
    target = ws / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    
def discard_workspace(ws) -> None:
    '''Borra la copia aislada (se usara al descartar o tras aplicar).'''
    ws = Path(ws)
    if ws.exists():
        shutil.rmtree(ws)