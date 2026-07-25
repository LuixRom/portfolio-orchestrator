from langchain_groq import ChatGroq

TIERS = {
    "easy":   {"provider": "groq","model": "openai/gpt-oss-20b"},
    "medium": {"provider": "groq","model": "openai/gpt-oss-120b"},
    "hard":   {"provider": "anthropic","model": "claude-sonnet-4-5"},
}

def get_llm(tier: str = "easy", temperature: float = 0.0):
    '''Devuelve el cliente del modelo correspondiente al tier.'''
    cfg = TIERS.get(tier)
    if cfg is None:
        raise ValueError(f"Tier desconocido: {tier!r}. Usa: {list(TIERS)}")

    if cfg["provider"] == "groq":
        return ChatGroq(model=cfg["model"], temperature=temperature)

    if cfg["provider"] == "anthropic":
        from langchain_anthropic import ChatAnthropic   # import local: solo si se usa
        return ChatAnthropic(model=cfg["model"], temperature=temperature)

    raise ValueError(f"Proveedor no soportado: {cfg['provider']}")
    