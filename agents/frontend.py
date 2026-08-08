from core.llm import get_llm
from pathlib import Path

def _cargar_skill(nombre: str) -> str:
    """Carga una skill bajo demanda desde la carpeta skills/."""
    ruta = Path(__file__).resolve().parent.parent / "skills" / f"{nombre}.md"
    if ruta.exists():
        return ruta.read_text(encoding="utf-8")
    return ""

def propose(instruction: str, profile: dict, current_content: str, tier: str = "medium") -> str:
    skill = _cargar_skill("frontend-design")
    '''Agente de FRONTEND: edita app/page.tsx (diseno y estructura de la pagina).

    'profile' se recibe para uniformidad con los demas agentes; por ahora trabaja
    con la instruccion y el page.tsx actual (que ya muestra que campos de 'site' hay).
    '''
    system = (
        f"{skill}\n\n"
        "Eres el agente de FRONTEND de un portafolio en Next.js (App Router) + "
        "TypeScript + Tailwind CSS. Recibes el archivo .tsx actual y devuelves "
        "el archivo COMPLETO ya modificado segun la instruccion. "
        "Responde EXCLUSIVAMENTE con el codigo .tsx, sin explicaciones ni ```."
    )
    user = f"INSTRUCCION:\n{instruction}\n\nPAGE.TSX ACTUAL:\n{current_content}"

    resp = get_llm(tier).invoke([
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ])

    texto = resp.content.strip().strip("`")
    for prefijo in ("tsx", "typescript", "jsx"):
        if texto.startswith(prefijo):
            texto = texto[len(prefijo):].strip()
    return texto