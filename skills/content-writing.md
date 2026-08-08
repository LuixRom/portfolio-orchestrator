---
name: content-writing
description: Redacta y mejora el contenido del portafolio profesional de Luis Anthony Romero Padilla. Úsala para hero, perfil, proyectos, experiencia, educación, certificaciones, contacto y textos de interfaz, siempre con información real y sin exageraciones.
---

# Content Writing

## Objetivo

Redactar contenido profesional, claro y específico que permita entender rápidamente:

- quién es Luis;
- qué sabe construir;
- qué experiencia posee;
- qué proyectos ha desarrollado;
- qué valor puede aportar.

El contenido debe sonar como un ingeniero explicando su trabajo, no como un vendedor promocionándose.

---

# 1. Fuente de verdad

Usar únicamente información real proporcionada en:

- el perfil del usuario;
- `content/site.json`;
- documentación del proyecto;
- información validada por el usuario.

Nunca inventar:

- proyectos;
- empleos;
- responsabilidades;
- fechas;
- métricas;
- resultados;
- certificaciones;
- tecnologías;
- clientes;
- niveles de dominio.

Si falta un dato, omitirlo.

No completar huecos con suposiciones.

---

# 2. Tono

El tono debe ser:

- profesional;
- directo;
- claro;
- honesto;
- específico;
- técnico cuando corresponda;
- fácil de entender.

Evitar:

- clichés;
- exageraciones;
- frases de marketing;
- adjetivos vacíos;
- lenguaje grandilocuente;
- emojis;
- relleno;
- afirmaciones difíciles de demostrar.

---

# 3. Palabras y frases que deben evitarse

Evitar expresiones como:

- apasionado por la tecnología;
- altamente motivado;
- innovador;
- experto;
- increíble;
- revolucionario;
- solución de vanguardia;
- resultados excepcionales;
- siempre aprendiendo;
- transformando ideas en realidad.

Estas frases solo pueden utilizarse cuando exista contexto concreto que las justifique, aunque normalmente deben sustituirse por hechos.

Incorrecto:

> Desarrollador apasionado que crea soluciones innovadoras.

Correcto:

> Estudiante de Ciencia de la Computación orientado al desarrollo de software, con experiencia en aplicaciones full stack, bases de datos y sistemas de inteligencia artificial.

---

# 4. Voz activa

Preferir verbos directos:

- desarrollé;
- implementé;
- diseñé;
- integré;
- construí;
- optimicé;
- automaticé;
- analicé;
- desplegué;
- documenté;
- validé.

Incorrecto:

> Se realizó la implementación de una API.

Correcto:

> Implementé una API REST para gestionar usuarios y autenticación.

En proyectos grupales, no atribuir al usuario el trabajo completo.

Usar:

> Participé en el desarrollo de…

o:

> Implementé el módulo de…

---

# 5. Hero

El hero debe ser breve.

Debe incluir:

- nombre;
- rol o dirección profesional;
- áreas principales;
- propuesta de valor clara;
- acción siguiente.

La descripción debe caber aproximadamente en dos o tres líneas en escritorio.

No colocar una biografía completa en el hero.

Ejemplo de estructura:

```text
Rol
Qué construye
Áreas principales
CTA
```

---

# 6. Sobre mí

La sección debe explicar:

- formación;
- dirección profesional;
- tipo de problemas que le interesa resolver;
- forma de trabajar;
- tecnologías o áreas relevantes.

No repetir literalmente:

- hero;
- CV;
- lista de tecnologías;
- contenido de proyectos.

Debe complementar el resto del portafolio.

---

# 7. Proyectos

Cada proyecto debe comunicar cuatro elementos:

1. Problema.
2. Solución.
3. Tecnologías.
4. Resultado o alcance verificable.

Formato recomendado:

> Sistema que [resuelve el problema] mediante [solución principal]. Implementado con [tecnologías relevantes] para [resultado, función o alcance].

No listar tecnologías sin explicar para qué fueron utilizadas.

No afirmar resultados si no existe evidencia.

## Proyectos colaborativos

Indicar con precisión:

- que fue trabajo en equipo;
- rol del usuario;
- módulos desarrollados;
- responsabilidades concretas.

No escribir:

> Construí un DBMS completo.

Cuando correspondió a un equipo.

Escribir:

> Participé en el desarrollo de un mini DBMS e implementé [módulos concretos].

---

# 8. Experiencia

Cada experiencia debe priorizar:

- responsabilidad;
- acción;
- herramienta;
- resultado verificable.

Cuando no existan métricas, describir el alcance real sin inventarlas.

Ejemplo:

> Desarrollé componentes reutilizables para el CRM y participé en la integración de formularios, validación y manejo de estado.

No convertir responsabilidades normales en supuestos logros extraordinarios.

---

# 9. Educación

Incluir:

- institución;
- programa;
- periodo;
- estado;
- detalle relevante.

No llenar la sección con todos los cursos.

Mencionar cursos únicamente cuando sean relevantes para el perfil o expliquen un proyecto destacado.

---

# 10. Certificaciones

Usar el nombre oficial.

Incluir:

- certificación;
- emisor;
- año;
- URL válida;
- detalle breve cuando aporte contexto.

No presentar cursos incompletos como certificaciones.

No convertir participación en un curso en dominio experto.

---

# 11. Stack tecnológico

Las tecnologías deben reflejar experiencia real.

No añadir una tecnología únicamente porque aparece una vez en una dependencia.

Ordenar por relevancia:

1. lenguajes;
2. frontend;
3. backend;
4. bases de datos;
5. inteligencia artificial y datos;
6. infraestructura;
7. herramientas.

Evitar niveles ambiguos como:

- experto;
- avanzado;
- intermedio;

salvo que el sistema requiera ese campo y exista criterio acordado.

---

# 12. Textos de interfaz

Los controles deben indicar claramente su acción.

Preferir:

- Ver proyectos;
- Descargar CV;
- Abrir repositorio;
- Ver demostración;
- Enviar mensaje;
- Copiar correo.

Evitar:

- Descubre más;
- Explora;
- Continuar;
- Enviar;
- Saber más;

cuando exista una acción más específica.

Mantener el mismo término durante todo el flujo.

Si un botón dice:

> Enviar mensaje

el estado final debe decir:

> Mensaje enviado

---

# 13. Errores y estados vacíos

Los errores deben explicar:

- qué ocurrió;
- qué puede hacer la persona.

Incorrecto:

> Algo salió mal.

Correcto:

> No se pudo enviar el mensaje. Revisa tu conexión e inténtalo nuevamente.

Los estados vacíos deben orientar hacia una acción.

---

# 14. Longitud

Preferir textos breves y densos en información.

Orientación:

- hero: 20–45 palabras;
- proyecto: 35–80 palabras;
- experiencia: 30–70 palabras;
- certificación: 10–30 palabras;
- CTA: 1–4 palabras.

No sacrificar claridad únicamente para cumplir una longitud.

---

# 15. Consistencia

Usar los mismos nombres para:

- tecnologías;
- instituciones;
- puestos;
- proyectos;
- acciones.

No alternar entre:

- Next y Next.js;
- Javascript y JavaScript;
- Postgres y PostgreSQL;

sin una razón concreta.

Mantener coherencia en:

- mayúsculas;
- puntuación;
- tiempos verbales;
- nombres propios.

---

# 16. Revisión final

Antes de guardar contenido, comprobar:

- ¿Todo es verificable?
- ¿Se inventó alguna métrica?
- ¿Hay frases genéricas?
- ¿El texto podría pertenecer a cualquier desarrollador?
- ¿Se entiende qué hizo Luis?
- ¿Se distingue el trabajo individual del grupal?
- ¿Hay repeticiones?
- ¿Las tecnologías aparecen con contexto?
- ¿El tono es profesional?
- ¿La información importante aparece primero?
- ¿El contenido cabe correctamente en la interfaz?

---

# Principio final

Ser específico es mejor que sonar impresionante.

La credibilidad del portafolio depende de mostrar trabajo real mediante explicaciones claras y verificables.