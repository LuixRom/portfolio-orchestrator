from core.llm import get_llm
from pathlib import Path
import json


def _cargar_agents_md() -> str:
    """Lee las convenciones del proyecto (AGENTS.md) para inyectarlas al prompt."""
    ruta = Path(__file__).resolve().parent.parent / "AGENTS.md"
    if ruta.exists():
        return ruta.read_text(encoding="utf-8")
    return ""


def propose(instruction: str, profile: dict, current_content: str, tier: str = "easy") -> str:
    """Genera el contenido nuevo del portafolio a partir de la instruccion.

    Recibe el perfil (datos reales) y el contenido actual, y devuelve el
    JSON completo ya modificado, como texto. Usa el tier indicado.
    """
    convenciones = _cargar_agents_md()

    system = (
        f"{convenciones}\n\n"
        "Eres el agente de contenido de un portafolio. Recibes el JSON de "
        "contenido actual y debes devolver el JSON COMPLETO ya modificado segun "
        "la instruccion. Usa SOLO datos reales del perfil; no inventes nada. "
        "Responde EXCLUSIVAMENTE con JSON valido, sin explicaciones ni ```."
    )

    user = (
        f"INSTRUCCION:\n{instruction}\n\n"
        f"PERFIL (datos reales):\n{json.dumps(profile, ensure_ascii=False)}\n\n"
        f"CONTENIDO ACTUAL:\n{current_content}"
    )

    resp = get_llm(tier).invoke([
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ])

    texto = resp.content.strip().strip("`")
    if texto.startswith("json"):
        texto = texto[4:].strip()
    return texto