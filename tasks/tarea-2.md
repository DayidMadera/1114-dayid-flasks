# Tarea 2 - Datos dinámicos en una plantilla Flask

## Objetivo

Aprender a pasar información desde el backend en Flask hacia una plantilla HTML. En esta tarea vas a dar un paso importante: pasar de una página estática a una plantilla que muestra datos generados en Python.

## Preparación

Antes de empezar, asegurate de tener funcionando el proyecto base y revisá el `README.md` si necesitás recordar cómo ejecutar la aplicación.

## Consigna

Modificá la función de la ruta `/` en `app.py` para que deje de renderizar una plantilla sin datos y empiece a enviar información a `render_template`.

La tarea debe cumplir con estos puntos:

1. Modificar la función asociada a la ruta `/` en `app.py`.
2. Pasar al menos 3 variables a `render_template`.
3. Mostrar esas variables dentro de `templates/index.html` con un propósito identificable en el contenido de la página.
4. Verificar el resultado final en el navegador.

Podés usar variables simples como un título, un nombre de usuario, un mensaje de bienvenida, una fecha en texto o una descripción corta.

## Foco técnico

En Flask, `render_template` permite enviar datos desde Python hacia una plantilla HTML. Esto importa porque marca el paso de un HTML fijo a una vista dinámica que responde a información definida en el backend.

En esta etapa, el foco está en entender la relación entre:

1. La función de la ruta en `app.py`.
2. Los argumentos enviados a `render_template`.
3. El uso de esas variables dentro de `templates/index.html`.

Todavía no hace falta trabajar con formularios, base de datos ni múltiples rutas.

## Preguntas de reflexión técnica

1. ¿Qué cambia en la plantilla cuando los datos llegan desde `app.py` en lugar de estar escritos directamente en el HTML?
2. ¿Qué ventaja tiene separar la lógica en Python de la presentación en la plantilla?
3. ¿Qué pasa si una variable no se envía desde `render_template`, pero se intenta mostrar en `index.html`?

## Entregable

Para dar la tarea por completa, se debe entregar:

1. `app.py` y `templates/index.html` actualizados.
2. Una verificación visual en el navegador de que los datos aparecen correctamente.
3. Una evidencia mínima indicando cuáles fueron las 3 variables usadas y en qué parte del HTML se muestra cada una.
