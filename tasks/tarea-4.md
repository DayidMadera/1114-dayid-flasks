# Tarea 4 - Mostrar listas con Jinja en Flask

## Objetivo

Agregar una seccion de recursos al Mini Portal de Clase Flask y mostrar una lista de elementos usando Jinja.

En las tareas anteriores ya trabajaste con una pagina inicial, datos simples y varias rutas. Ahora vas a dar otro paso importante: enviar una lista desde Python y recorrerla en una plantilla HTML.

## Preparacion

Antes de empezar, asegurate de tener completada la tarea 3.

El proyecto deberia tener al menos estas rutas funcionando:

1. `/`
2. `/acerca`
3. `/contacto`

Tambien deberias poder navegar entre esas paginas desde el navegador.

## Consigna

Crea una nueva seccion llamada Recursos.

La tarea debe cumplir con estos puntos:

1. Crear una ruta `/recursos` en `app.py`.
2. Crear una plantilla `templates/recursos.html`.
3. Crear una lista en Python con al menos 4 recursos de clase.
4. Enviar esa lista a la plantilla usando `render_template`.
5. Recorrer la lista en `recursos.html` usando un bucle `{% for %}` de Jinja.
6. Mostrar cada recurso dentro de una lista HTML (`<ul>` o `<ol>`).
7. Agregar un enlace de navegacion hacia Recursos desde las demas paginas.
8. Verificar el resultado final en el navegador.

Los recursos pueden ser temas, enlaces, herramientas o materiales de clase. Por ejemplo:

1. Entorno virtual
2. Rutas en Flask
3. Plantillas HTML
4. Variables con Jinja

## Foco tecnico

Hasta ahora mostraste datos simples como textos individuales. Pero muchas aplicaciones web necesitan mostrar colecciones: productos, usuarios, tareas, mensajes, cursos o recursos.

En Python, una lista puede verse asi:

```python
recursos = ["Entorno virtual", "Rutas en Flask", "Plantillas HTML"]
```

Y en una plantilla Jinja se puede recorrer asi:

```html
{% for recurso in recursos %}
  <li>{{ recurso }}</li>
{% endfor %}
```

Ese recorrido significa:

1. Flask prepara una lista en Python.
2. Flask envia esa lista a la plantilla.
3. Jinja repite una parte del HTML por cada elemento.
4. El navegador recibe HTML final ya generado.

Ojo con esto: el navegador no entiende Jinja. Jinja se procesa antes, del lado de Flask. Lo que llega al navegador es HTML normal.

## Preguntas de reflexion tecnica

1. Que diferencia hay entre mostrar una variable simple y recorrer una lista?
2. Donde existe primero la lista: en Python, en Jinja o en el navegador?
3. Que hace `{% for recurso in recursos %}`?
4. Que muestra `{{ recurso }}` dentro del bucle?
5. Que pasaria si la lista esta vacia?
6. Por que este concepto sirve para mostrar productos, alumnos, tareas o mensajes en una aplicacion real?

## Entregable

Para dar la tarea por completa, se debe entregar:

1. `app.py` con la ruta `/recursos`.
2. `templates/recursos.html` creado y funcionando.
3. Una lista de al menos 4 recursos definida en Python.
4. La lista renderizada en HTML usando `{% for %}`.
5. Navegacion hacia la nueva pagina Recursos.
6. Una explicacion corta del flujo: `lista en Python -> render_template -> bucle en Jinja -> HTML final`.

## Tiempo estimado

Esta tarea deberia tomar entre 60 y 90 minutos.

Si ya entendiste bien las rutas de la tarea 3, probablemente la parte nueva sea solo el bucle. Si todavia te cuesta conectar rutas y plantillas, tomate mas tiempo. No corras. Primero entende el recorrido.

## Cierre

Esta tarea marca un salto importante: ya no estas mostrando una pagina fija ni datos sueltos. Estas empezando a renderizar colecciones.

Muchas aplicaciones reales son, en el fondo, esto mismo: traer una lista de datos y mostrarla de forma clara en una pagina.
