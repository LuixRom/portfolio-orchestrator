import json
from pathlib import Path
from pydantic import BaseModel, Field

class Perfil(BaseModel):
    nombre: str
    titulo: str
    resumen: str
    ubicacion: str | None = None
    nivel_ingles: str | None = None


class Contacto(BaseModel):
    email: str
    linkedin: str
    github: str


class Proyecto(BaseModel):
    nombre: str
    descripcion: str
    stack: list[str] = Field(default_factory=list)
    destacado: bool = False


class Profile(BaseModel):
    perfil: Perfil
    contacto: Contacto
    proyectos: list[Proyecto] = Field(default_factory=list)
    experiencia: list[dict] = Field(default_factory=list)
    habilidades: dict = Field(default_factory=dict)
    
    
def load_profile(path: str = "data/profile.json") -> Profile:
    '''Carga y VALIDA profile.json. Si falta un campo o hay un tipo mal, lanza un error claro en vez de fallar silenciosamente mas adelante.'''
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return Profile.model_validate(data)