# Tarea 3 - Crear varias rutas y varias paginas en Flask

## Objetivo

Convertir el proyecto en un Mini Portal de Clase Flask con mas de una pagina.

Hasta ahora trabajaste con una sola ruta: `/`. En esta tarea vas a entender que una aplicacion Flask puede responder a distintas URL, y que cada URL puede ejecutar una funcion diferente y mostrar una plantilla diferente.

## Preparacion

Antes de empezar, asegurate de que el proyecto corre correctamente con:

```powershell
python app.py
```

Luego abri la aplicacion en el navegador y verifica que la ruta principal `/` funciona.

## Consigna

Agrega nuevas secciones al portal usando rutas y plantillas.

La tarea debe cumplir con estos puntos:

1. Mantener funcionando la ruta principal `/`.
2. Crear una ruta `/acerca` en `app.py`.
3. Crear una ruta `/contacto` en `app.py`.
4. Crear una plantilla `templates/acerca.html`.
5. Crear una plantilla `templates/contacto.html`.
6. Agregar enlaces de navegacion para moverse entre Inicio, Acerca y Contacto.
7. Verificar cada pagina desde el navegador.

## Foco tecnico

En Flask, una ruta conecta una URL con una funcion de Python.

Por ejemplo:

```python
@app.route("/acerca")
def acerca():
    return render_template("acerca.html")
```

Ese codigo significa:

1. Cuando el navegador pide `/acerca`, Flask ejecuta la funcion `acerca()`.
2. La funcion devuelve una plantilla HTML.
3. Flask busca esa plantilla dentro de la carpeta `templates`.
4. El navegador muestra el resultado.

No memorices el decorador. Entende el recorrido. La programacion web se aprende entendiendo el flujo, no copiando bloques sueltos.

## Preguntas de reflexion tecnica

1. Que relacion hay entre `/acerca`, la funcion `acerca()` y el archivo `acerca.html`?
2. Que pasaria si la ruta existe en `app.py`, pero el archivo HTML no existe en `templates`?
3. Que pasaria si el archivo HTML existe, pero no hay ninguna ruta que lo renderice?
4. Por que conviene separar una pagina en su propia plantilla en lugar de poner todo en `index.html`?
5. Que evidencia te da el navegador de que cada ruta esta funcionando?

## Entregable

Para dar la tarea por completa, se debe entregar:

1. `app.py` con las rutas `/`, `/acerca` y `/contacto`.
2. Las plantillas `index.html`, `acerca.html` y `contacto.html` funcionando.
3. Navegacion entre las tres paginas.
4. Una explicacion corta del flujo de una ruta completa, por ejemplo: `/contacto -> contacto() -> contacto.html`.

## Cierre

Ahora el proyecto ya no es una pagina suelta. Empieza a comportarse como una aplicacion web real: varias URL, varias funciones y varias vistas conectadas por una misma idea.

Ese es el salto importante de esta tarea.
