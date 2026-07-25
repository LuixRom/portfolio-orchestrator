'''Configuracion TECNICA (separada de profile.json, que es solo contenido).'''

CONTENT_FILE = "content/site.json"
VALIDATION_COMMANDS: list[list[str]] = []
MAX_RETRIES = 2
ESCALATE_AFTER_FAILURES = 1