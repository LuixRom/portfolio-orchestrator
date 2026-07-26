from core.llm import get_llm


def propose(instruction: str, profile: dict, current_content: str, tier: str = "medium") -> str:
    '''Agente de FRONTEND: edita app/page.tsx (diseno y estructura de la pagina).

    'profile' se recibe para uniformidad con los demas agentes; por ahora trabaja
    con la instruccion y el page.tsx actual (que ya muestra que campos de 'site' hay).
    '''
    system = (
        "Eres el agente de FRONTEND de un portafolio en Next.js (App Router) + "
        "TypeScript + Tailwind CSS. Recibes el archivo page.tsx actual y devuelves "
        "el archivo COMPLETO ya modificado segun la instruccion.\n\n"
        "Reglas obligatorias:\n"
        "1. Conserva SIEMPRE la linea 'import site from \"@/content/site.json\"' y "
        "sigue mostrando los textos desde el objeto 'site'. No escribas como texto "
        "fijo lo que deberia venir del JSON.\n"
        "2. Usa solo clases de Tailwind para el estilo.\n"
        "3. El codigo debe ser TSX valido y compilable.\n"
        "4. Responde EXCLUSIVAMENTE con el codigo .tsx, sin explicaciones ni ```."
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