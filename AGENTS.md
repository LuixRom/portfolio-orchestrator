# AGENTS.md — Convenciones del Portafolio

Eres un agente encargado de editar y mantener el portafolio profesional de Luis Anthony Romero Padilla.

Tu objetivo es mejorar el proyecto sin alterar su identidad, estructura ni calidad.

---

# 1. Filosofía del proyecto

Este portafolio prioriza:

- Claridad sobre complejidad.
- Calidad sobre cantidad.
- Mantenibilidad sobre soluciones rápidas.
- Rendimiento sobre efectos visuales innecesarios.
- Información real sobre contenido de marketing.

Cada modificación debe hacer que el portafolio sea más profesional, consistente y fácil de mantener.

Cuando existan varias soluciones válidas, elige siempre la más simple.

---

# 2. Prioridad de instrucciones

En caso de conflicto sigue este orden:

1. La instrucción del usuario.
2. Este archivo AGENTS.md.
3. La arquitectura existente del proyecto.
4. El estilo ya implementado.

Nunca ignores una instrucción de mayor prioridad.

---

# 3. Idioma y estilo

Todo el contenido visible para el usuario debe escribirse en español.

El tono debe ser:

- Profesional.
- Directo.
- Claro.
- Conciso.

Evita:

- exageraciones
- frases de marketing
- clichés
- emojis
- texto de relleno
- afirmaciones sin evidencia

Escribe como un ingeniero, no como un vendedor.

---

# 4. Datos

Usa únicamente información real proporcionada por el usuario.

Nunca inventes:

- proyectos
- empleos
- tecnologías
- fechas
- certificaciones
- logros
- métricas
- clientes
- porcentajes
- experiencia laboral

Si un dato no existe:

- omítelo
- o conserva el valor existente

Nunca lo inventes.

Los campos cuyo nombre termine en:

- `_editable`
- `nota_editable`

son únicamente recordatorios internos.

Nunca deben mostrarse en la interfaz ni utilizarse como contenido real.

---

# 5. Principio de preservación

Conserva todo el contenido existente que no esté relacionado con la solicitud.

Nunca elimines información porque "parezca innecesaria".

Nunca simplifiques estructuras sin autorización.

Realiza siempre el cambio mínimo necesario para cumplir la petición.

---

# 6. Estructura de content/site.json

No modificar la estructura.

Las claves existentes deben mantenerse.

No cambiar tipos de datos.

No renombrar propiedades.

No agregar nuevas claves salvo que el usuario lo solicite explícitamente.

Conservar las siguientes estructuras:

- perfil
- hero
- stats
- sobre_mi
- proyectos
- experiencia
- educacion
- tech_stack
- certificaciones
- contacto
- redes

Respetar exactamente el tipo de cada propiedad.

---

# 7. Reglas para contenido

Cada proyecto debe describir:

- problema
- solución
- tecnologías utilizadas

Evitar descripciones genéricas.

Incorrecto:

"Proyecto increíble."

Correcto:

"Aplicación web para gestionar inventario utilizando Next.js y PostgreSQL."

Las tecnologías deben ordenarse por importancia.

Ejemplo:

Frontend

Backend

Base de datos

Infraestructura

Herramientas

---

# 8. Reglas para frontend

El contenido debe obtenerse desde:

content/site.json

No escribir textos fijos cuando deban provenir del JSON.

Mantener componentes reutilizables.

Evitar duplicar contenido.

Evitar duplicar componentes.

Reutilizar componentes existentes cuando sea posible.

---

# 9. Reglas de diseño

La identidad visual del portafolio debe mantenerse.

Principios:

- minimalista
- moderna
- tecnológica
- profesional
- consistente

Evitar:

- glassmorphism excesivo
- gradientes exagerados
- animaciones innecesarias
- sombras muy intensas
- efectos que reduzcan el rendimiento

Los efectos visuales deben ser discretos y aportar valor a la experiencia.

---

# 10. Rendimiento

No introducir librerías pesadas sin justificación.

Preferir:

- CSS
- SVG
- componentes reutilizables

antes que soluciones complejas en JavaScript.

Evitar renderizados innecesarios.

Priorizar la velocidad de carga.

---

# 11. Accesibilidad

Mantener siempre:

- contraste adecuado
- navegación mediante teclado
- estados focus visibles
- atributos aria cuando correspondan
- diseño responsive

No eliminar características de accesibilidad existentes.

---

# 12. Calidad del código

Antes de crear un nuevo componente:

1. Verifica si ya existe uno equivalente.
2. Reutilízalo si es posible.

Mantener:

- nombres claros
- componentes pequeños
- separación de responsabilidades
- consistencia con la arquitectura existente

No introducir deuda técnica innecesaria.

---

# 13. Validación

Antes de finalizar cualquier modificación verifica:

Contenido

- No se inventó información.
- No se eliminó contenido sin autorización.

JSON

- JSON válido.
- Sin claves duplicadas.
- Sin cambios de tipo.
- Sin propiedades inesperadas.

Frontend

- Sin errores de compilación.
- Sin imports sin usar.
- Sin componentes rotos.
- Responsive conservado.

---

# 14. Alcance de las tareas

## Contenido

Las tareas de contenido modifican únicamente:

content/site.json

## Frontend

Las tareas de frontend modifican únicamente:

- componentes
- páginas
- estilos
- animaciones

sin romper la separación entre presentación y contenido.

---

# 15. Restricciones

Nunca:

- inventar información
- eliminar contenido sin autorización
- romper la estructura del JSON
- duplicar componentes
- cambiar la identidad visual del portafolio sin solicitud explícita
- introducir dependencias pesadas sin justificación

---

# 16. Objetivo final

Cada cambio debe cumplir simultáneamente estos principios:

- mantener la identidad del portafolio;
- mejorar la experiencia del usuario;
- conservar una arquitectura limpia;
- facilitar el mantenimiento futuro;
- producir un resultado profesional, consistente y sostenible.