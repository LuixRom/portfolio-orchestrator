import shutil
import difflib
from pathlib import Path


PORTFOLIO_DIR = Path(__file__).resolve().parent.parent.parent / "portfolio-web"
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent / ".workspaces"

def create_workspace(run_id: str) -> Path:
    """Crea un workspace VACIO. Ya no copiamos el proyecto: solo escribiremos
    ahi el/los archivo(s) propuestos, asi la operacion es instantanea."""
    WORKSPACE_ROOT.mkdir(parents=True, exist_ok=True)
    ws = WORKSPACE_ROOT / run_id
    if ws.exists():
        shutil.rmtree(ws)
    ws.mkdir(parents=True, exist_ok=True)
    return ws

def read_current(rel: str) -> str:
    """Lee el contenido ACTUAL de un archivo desde main. Leer no muta main."""
    return (PORTFOLIO_DIR / rel).read_text(encoding="utf-8")

def write_file(ws: Path, rel: str, content: str) -> None:
    """Escribe la propuesta SOLO en el workspace (jamas en main)."""
    target = ws / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    
def make_diff(ws: Path, rel: str) -> str:
    """Diff unificado del archivo entre main y el workspace."""
    main_path = PORTFOLIO_DIR / rel
    old = main_path.read_text(encoding="utf-8").splitlines(keepends=True) if main_path.exists() else []
    new = (ws / rel).read_text(encoding="utf-8").splitlines(keepends=True)
    diff = difflib.unified_diff(old, new, fromfile=f"main/{rel}", tofile=f"workspace/{rel}")
    return "".join(diff) or "(sin cambios)"

def apply_workspace(ws, changed: list) -> None:
    """Vuelca los archivos cambiados del workspace sobre main. Solo tras tu aprobacion."""
    ws = Path(ws)
    for rel in changed:
        src = ws / rel
        dst = PORTFOLIO_DIR / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        
def discard_workspace(ws) -> None:
    ws = Path(ws)
    if ws.exists():
        shutil.rmtree(ws)