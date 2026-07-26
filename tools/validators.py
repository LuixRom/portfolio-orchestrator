import json
import subprocess
from pathlib import Path
from settings import CONTENT_FILE, VALIDATION_COMMANDS

def _check_content_json(ws) -> dict:
    from pathlib import Path
    path = Path(ws) / CONTENT_FILE
    if not path.exists():
        return {"check": "json", "ok": True, "detalle": "no aplica (no se edito site.json)"}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return {"check": "json", "ok": False, "detalle": f"JSON invalido: {e}"}
    faltan = [k for k in ("hero", "secciones") if k not in data]
    if faltan:
        return {"check": "estructura", "ok": False, "detalle": f"faltan claves: {faltan}"}
    return {"check": "json_y_estructura", "ok": True, "detalle": "ok"}

def _run_command(ws: Path, cmd: list[str]) -> dict:
    '''Ejecuta un comando externo (lint/build/tests) DENTRO del workspace.'''
    try:
        proc = subprocess.run(cmd, cwd=ws, capture_output=True, text=True, timeout=300)
        return {"check": " ".join(cmd), "ok": proc.returncode == 0,
                "detalle": (proc.stderr or proc.stdout)[-500:]}
    except Exception as e:
        return {"check": " ".join(cmd), "ok": False, "detalle": str(e)}
    
def run_validations(ws) -> dict:
    '''Corre todas las validaciones y devuelve un resumen. Determinista, sin LLM.'''
    ws = Path(ws)
    checks = [_check_content_json(ws)]
    for cmd in VALIDATION_COMMANDS:
        checks.append(_run_command(ws, cmd))

    ok = all(c["ok"] for c in checks)
    return {"ok": ok, "checks": checks}