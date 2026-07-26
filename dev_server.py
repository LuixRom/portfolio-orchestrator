"""Arranca el servidor de LangGraph igual que `langgraph dev`, pero excluyendo
del watcher las carpetas que no son codigo fuente (.workspaces, .venv,
node_modules, .git, .langgraph_api). Sin esto, cualquier archivo generado ahi
dispara recargas en cascada y puede terminar en PermissionError/CancelledError.

Uso: python dev_server.py
"""
import pathlib
import sys

import langgraph_cli.config
from langgraph_api.cli import run_server

CONFIG_PATH = pathlib.Path("langgraph.json")

RELOAD_EXCLUDES = [
    "*/.workspaces/*",
    "*/.venv/*",
    "*/node_modules/*",
    "*/.git/*",
    "*/.langgraph_api/*",
]

if __name__ == "__main__":
    # uvicorn --reload arranca un subproceso con multiprocessing; en Windows
    # (spawn) eso reimporta este modulo, asi que todo el setup debe quedar
    # dentro de este guard o el subproceso vuelve a llamar run_server().
    config_json = langgraph_cli.config.validate_config_file(CONFIG_PATH)

    cwd = pathlib.Path.cwd()
    sys.path.append(str(cwd))
    for dep in config_json.get("dependencies", []):
        dep_path = cwd / dep
        if dep_path.is_dir():
            sys.path.append(str(dep_path))

    run_server(
        host="127.0.0.1",
        port=2024,
        reload=True,
        graphs=config_json.get("graphs", {}),
        open_browser=True,
        env=config_json.get("env"),
        store=config_json.get("store"),
        auth=config_json.get("auth"),
        http=config_json.get("http"),
        ui=config_json.get("ui"),
        ui_config=config_json.get("ui_config"),
        webhooks=config_json.get("webhooks"),
        checkpointer=config_json.get("checkpointer"),
        disable_persistence=config_json.get("disable_persistence", False),
        reload_excludes=RELOAD_EXCLUDES,
    )
