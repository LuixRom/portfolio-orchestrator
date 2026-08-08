---
name: frontend-design
description: Diseña, implementa y mantiene la interfaz del portafolio profesional de Luis Anthony Romero Padilla. Úsala para tareas de layout, componentes, React, Next.js, Tailwind CSS, responsive design, accesibilidad, animaciones, rendimiento e identidad visual.
---

# Frontend Design

## Objetivo

Construir y mantener un portafolio profesional que comunique madurez técnica, claridad y atención al detalle.

El sitio debe transmitir:

> Este desarrollador construye software bien diseñado y mantenible.

No debe transmitir:

> Este sitio intenta impresionar mediante efectos visuales excesivos.

El diseño debe ser reconocible, moderno y tecnológico, sin parecer una plantilla genérica de inteligencia artificial, una página de videojuegos, una landing de criptomonedas ni un dashboard futurista recargado.

---

# 1. Identidad visual

La interfaz debe sentirse:

- moderna;
- profesional;
- tecnológica;
- sobria;
- precisa;
- oscura;
- elegante;
- coherente.

Debe conservar la estructura original del portafolio y mejorarla mediante detalles visuales cuidadosamente seleccionados.

No copiar literalmente diseños de referencia. Extraer principios, patrones y recursos visuales, y adaptarlos a la identidad existente.

---

# 2. Sistema de color

Usar esta paleta como base:

```text
Background principal:  #090B10
Surface principal:     #11151D
Surface elevada:       #151A24
Border sutil:          #202838

Texto principal:       #F5F7FA
Texto secundario:      #9CA7B8
Texto tenue:           #667085

Acento principal:      #5B7CFF
Acento hover:          #7A95FF
Acento secundario:     #38D9FF
```

El acento secundario debe utilizarse con moderación.

No convertir la interfaz en una composición multicolor.

El color principal debe aparecer principalmente en:

- navegación activa;
- botones principales;
- enlaces;
- indicadores;
- etiquetas importantes;
- barras de sección;
- bordes interactivos;
- estados de hover y focus.

---

# 3. Firma visual

La firma visual del portafolio será una combinación de:

- una barra vertical o línea de acento índigo;
- brillos ambientales suaves;
- tarjetas oscuras con bordes discretos;
- pequeñas líneas técnicas;
- indicadores de estado;
- tipografía clara;
- composición limpia.

La barra de acento debe utilizarse para reforzar jerarquía, no como decoración repetitiva en todos los elementos.

Un solo recurso memorable bien ejecutado es mejor que muchos efectos compitiendo entre sí.

---

# 4. Fondos y brillo

Los brillos deben ser ambientales y sutiles.

Preferir CSS:

```css
background:
  radial-gradient(
    circle at center,
    rgba(91, 124, 255, 0.12),
    transparent 55%
  );
```

Ejemplo de glow:

```css
box-shadow:
  0 0 60px rgba(91, 124, 255, 0.12);
```

Evitar:

- resplandores intensos en todas las tarjetas;
- sombras azules en cada elemento;
- fondos saturados;
- partículas permanentes;
- efectos que dificulten la lectura.

Los fondos pueden incluir líneas, puntos, ruido o gradientes radiales siempre que tengan poca opacidad y no distraigan.

---

# 5. Hero

El hero es la tesis visual y profesional del portafolio.

Debe responder rápidamente:

- quién es Luis;
- qué construye;
- en qué áreas trabaja;
- por qué vale la pena seguir explorando.

Debe priorizar:

- nombre;
- rol;
- descripción breve;
- CTA principal;
- CTA secundario;
- estado de disponibilidad si existe.

No usar estadísticas genéricas, números decorativos o gradientes por defecto salvo que aporten información real.

Se permite un efecto visual especial en el hero, pero debe existir solo uno:

- glow ambiental;
- cursor interactivo suave;
- texto con reveal;
- línea técnica animada;
- fondo radial;
- elemento visual relacionado con código o software.

---

# 6. Tipografía

La tipografía debe aportar personalidad sin reducir la legibilidad.

Mantener:

- una familia principal para cuerpo;
- una familia o peso distintivo para títulos;
- una fuente monoespaciada para datos, etiquetas técnicas o fragmentos de código.

Evitar utilizar demasiadas familias.

La jerarquía debe ser clara mediante:

- tamaño;
- peso;
- ancho;
- espaciado;
- contraste.

No depender solo del color para diferenciar niveles de información.

---

# 7. Layout y jerarquía

Cada sección debe tener un propósito claro.

La estructura principal puede incluir:

- Home;
- About;
- Projects;
- Experience;
- Education;
- Certifications;
- Contact.

Priorizar una composición equilibrada con suficiente espacio negativo.

No llenar cada espacio vacío con elementos decorativos.

El diseño puede utilizar:

- sidebar en escritorio;
- navegación compacta en móvil;
- grid para proyectos;
- timeline para experiencia;
- bloques editoriales;
- tarjetas destacadas;
- separadores técnicos.

La estructura debe adaptarse al contenido real, no forzar el contenido a una plantilla.

---

# 8. Proyectos

Los proyectos son el centro del portafolio.

Cada tarjeta debe mostrar claramente:

- nombre;
- categoría;
- descripción;
- stack;
- repositorio;
- demo cuando exista;
- estado destacado cuando corresponda.

Las tecnologías deben mostrarse como etiquetas compactas.

No usar tarjetas gigantes para proyectos pequeños.

Evitar múltiples estilos de tarjeta. Mantener una base consistente y permitir una variante destacada.

Los efectos de hover pueden incluir:

- ligero desplazamiento vertical;
- cambio de borde;
- glow reducido;
- aparición de acciones;
- cambio sutil de fondo.

No rotar, inclinar excesivamente ni aplicar efectos 3D innecesarios.

---

# 9. Experiencia y educación

Usar timeline únicamente cuando el orden temporal sea importante.

Las líneas, nodos y fechas deben representar información real.

No utilizar numeración decorativa como `01`, `02`, `03` salvo que el contenido sea realmente secuencial.

La universidad puede integrarse mediante:

- marca de agua tenue;
- texto de gran escala detrás del contenido;
- sello visual;
- bloque editorial;
- etiqueta institucional;
- línea temporal.

Si se usa texto grande de fondo, debe tener baja opacidad y no afectar la lectura.

---

# 10. Motion

La animación debe explicar jerarquía, cambio o interacción.

Usos recomendados:

- reveal de sección;
- hover de tarjeta;
- feedback de botón;
- transición de navegación;
- aparición progresiva del hero;
- cambio de filtro;
- entrada de elementos al viewport.

Evitar:

- animaciones infinitas;
- rebotes;
- iconos girando;
- paralaje excesivo;
- animar todos los elementos;
- retrasos largos;
- movimientos que bloqueen la interacción.

Una animación orquestada es mejor que muchos efectos pequeños sin relación.

Respetar siempre:

```css
@media (prefers-reduced-motion: reduce)
```

---

# 11. Librerías visuales

Preferir este orden:

1. CSS y Tailwind.
2. SVG.
3. Framer Motion para animaciones justificadas.
4. Componentes locales reutilizables.
5. Librerías externas solo cuando resuelvan un problema real.

Librerías permitidas cuando aporten valor:

- Framer Motion;
- Lucide React;
- shadcn/ui;
- componentes puntuales de Magic UI o React Bits;
- Lenis únicamente si el scroll actual lo justifica.

Evitar introducir:

- Three.js;
- GSAP;
- OGL;
- sistemas de partículas;
- múltiples librerías de animación;

salvo solicitud explícita y validación de rendimiento.

No instalar una librería completa para usar un solo efecto que pueda reproducirse con CSS.

---

# 12. React y Next.js

## Componentes

- Preferir componentes pequeños y reutilizables.
- Mantener una responsabilidad principal por componente.
- Evitar archivos excesivamente grandes.
- Usar composición antes que duplicación.
- Buscar componentes existentes antes de crear nuevos.

## Datos

El contenido debe leerse desde:

```text
content/site.json
```

No escribir contenido fijo en componentes cuando corresponda al JSON.

## Estado

- Mantener el estado local cuando sea posible.
- No introducir estado global sin necesidad.
- Preferir props para flujos simples.
- Evitar contextos para datos que solo usan uno o dos componentes.

## Server y Client Components

En Next.js:

- usar Server Components por defecto;
- añadir `"use client"` solo cuando exista interactividad real;
- evitar convertir árboles completos en componentes cliente;
- mantener las dependencias del navegador cerca del componente que las necesita.

## Rendimiento

- No utilizar memoización sin evidencia.
- Evitar renders innecesarios.
- Cargar de forma diferida componentes pesados.
- Optimizar imágenes.
- No importar paquetes completos cuando existan imports individuales.
- Evitar JavaScript para efectos posibles con CSS.

---

# 13. Tailwind CSS

## Tokens

Reutilizar variables y clases del sistema visual.

Evitar valores arbitrarios repetidos como:

```text
mt-[37px]
text-[#5B7CFF]
shadow-[...]
```

Si un valor se repite, convertirlo en token, variable o utilidad reutilizable.

## Espaciado

Usar un sistema basado principalmente en múltiplos de 4 y 8 px.

Mantener consistencia entre:

- secciones;
- tarjetas;
- encabezados;
- grids;
- componentes.

## Layout

Preferir:

- `grid`;
- `flex`;
- `gap`;
- `max-w-*`;
- `mx-auto`;

antes que offsets manuales.

Evitar wrappers sin propósito.

## Orden de utilidades

Mantener un orden legible:

1. layout;
2. posición;
3. tamaño;
4. espaciado;
5. tipografía;
6. color;
7. borde;
8. sombra y efectos;
9. interacción;
10. responsive.

## Responsive

Diseñar mobile first.

Validar al menos:

- móvil pequeño;
- móvil grande;
- tablet;
- escritorio;
- escritorio amplio.

No ocultar contenido importante solo para resolver problemas responsive.

---

# 14. Código y mantenibilidad

Preferir soluciones simples y explícitas.

Evitar abstracciones anticipadas.

Usar nombres descriptivos.

Convenciones:

- componentes: `PascalCase`;
- variables y funciones: `camelCase`;
- constantes globales: `UPPER_SNAKE_CASE` solo cuando corresponda;
- archivos de componentes: nombre del componente;
- hooks: prefijo `use`.

Eliminar imports y código sin uso.

Comentar el motivo de una decisión, no describir una línea evidente.

Mantener una responsabilidad clara por archivo.

No introducir una arquitectura nueva si el problema puede resolverse dentro de la existente.

---

# 15. Accesibilidad

Usar HTML semántico.

- `button` para acciones;
- `a` para navegación;
- headings en orden lógico;
- landmarks cuando correspondan;
- labels visibles o accesibles;
- estados focus visibles;
- contraste suficiente;
- alt text útil;
- navegación por teclado.

No usar `div` interactivos cuando exista un elemento semántico apropiado.

No eliminar outline sin reemplazarlo con un focus visible.

---

# 16. Proceso de trabajo

Antes de editar:

1. Identificar la tarea exacta.
2. Revisar la estructura existente.
3. Localizar componentes reutilizables.
4. Confirmar qué contenido proviene de `site.json`.
5. Definir el cambio mínimo necesario.

Para tareas de rediseño:

1. Definir una propuesta corta.
2. Establecer colores, tipografía, layout y elemento distintivo.
3. Comparar la propuesta con el diseño actual.
4. Eliminar decisiones que parezcan genéricas o copiadas.
5. Implementar.
6. Revisar visualmente.
7. Quitar al menos un elemento innecesario.

---

# 17. Autocrítica

Antes de finalizar, comprobar:

- ¿Parece una plantilla genérica?
- ¿Mantiene la identidad original?
- ¿Hay demasiados efectos?
- ¿Se entiende la información en pocos segundos?
- ¿La jerarquía es clara?
- ¿Los componentes parecen pertenecer al mismo sistema?
- ¿La página sigue siendo rápida?
- ¿El diseño funciona sin animaciones?
- ¿El resultado es accesible?
- ¿Se agregó una dependencia innecesaria?
- ¿Hay código duplicado?
- ¿El cambio podría ser más simple?

---

# Principio final

La creatividad debe concentrarse en pocos detalles memorables.

El resto de la interfaz debe permanecer clara, rápida, mantenible y profesional.

La meta no es construir el portafolio más recargado.

La meta es construir un portafolio que demuestre criterio técnico y visual.