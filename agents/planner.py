from settings import ESCALATE_AFTER_FAILURES


def choose_tier(task_type: str, complexity: str, retry_count: int) -> tuple[str, str]:
    '''
        Decide el tier segun tu regla. Devuelve (tier, motivo).

        Sonnet (hard) SOLO por: arquitectura, complejidad alta, o fallos repetidos.
        Lo normal se queda en 120B (medium) o, si es trivial, 20B (easy).
    '''
    if task_type=="architecture":
        return "hard", "tarea de arquitectura"
    if complexity=="high":
        return "hard", "complejidad alta"
    if retry_count >= ESCALATE_AFTER_FAILURES:
        return "hard", f"fallos repetidos ({retry_count})"

    if complexity == "low":
        return "easy", "tarea simple -> 20B"
    return "medium", "tarea normal -> 120B"