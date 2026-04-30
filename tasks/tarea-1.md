# Tarea 1 - Levantar una aplicacion Flask desde cero

## Objetivo tecnico

Poner en marcha el proyecto en tu entorno local, entender para que sirve cada pieza minima del setup y verificar que la aplicacion responde en el navegador.

En esta primera clase no alcanza con "hacerlo andar". Tienes que empezar a distinguir que problema resuelve cada paso: aislamiento del entorno, instalacion de dependencias, arranque del servidor y renderizado de una plantilla HTML.

## Preparacion

Para instalar dependencias y ejecutar el proyecto, sigue el `README.md`.

## Consigna

1. Instala las dependencias y levanta la aplicacion siguiendo el `README.md`.

2. Abre la aplicacion en el navegador y comprueba que responde correctamente.

3. Modifica la vista base y verifica el cambio:

   Edita `templates/index.html`, cambia al menos el `<title>` y el `<h1>`, guarda y recarga la pagina.

   Este paso existe para que veas la relacion concreta entre archivo fuente, servidor y resultado en navegador. Codigo que no observas, no lo entendes.

## Preguntas de reflexion tecnica
1. ¿Qué problema resuelve el entorno virtual en un proyecto Python?
El entorno virtual me permite aislar las dependencias de mi proyecto. Así evito conflictos con otras versiones de librerías que tenga instaladas en mi sistema o en otros proyectos.

2. ¿Qué diferencia hay entre instalar Flask globalmente y hacerlo dentro de .venv?
Si instalo Flask globalmente, queda disponible para todo el sistema, lo que puede generar conflictos con otros proyectos. En cambio, si lo instalo dentro de .venv, solo ese proyecto usa esa versión específica, lo cual es más ordenado y seguro.

3. ¿Por qué requirements.txt forma parte del proyecto y no de mi máquina personal?
Porque ahí defino las dependencias necesarias para que el proyecto funcione. Esto permite que cualquier otra persona o servidor pueda instalar exactamente lo mismo y ejecutar el proyecto sin problemas.

4. ¿Cuando ejecuto python app.py, qué archivo actúa como punto de entrada y por qué?
El archivo app.py es el punto de entrada porque es el que ejecuto directamente. Además, contiene la configuración de la aplicación y el bloque que arranca el servidor.

5. ¿Qué relación hay entre la ruta /, la función inicio() y el archivo templates/index.html?
La ruta / está asociada a la función inicio(). Cuando alguien entra a esa ruta, Flask ejecuta esa función, y esta devuelve el archivo templates/index.html, que es lo que finalmente se muestra en el navegador.

6. ¿Qué evidencia me da la terminal de que el servidor arrancó correctamente?
La terminal muestra un mensaje indicando que el servidor está corriendo, como “Running on http://127.0.0.1:5000/”
. Eso confirma que todo está funcionando.

7. Si cambio el HTML y el navegador muestra otra cosa, ¿qué me demuestra eso?
Me demuestra que hay una conexión correcta entre el backend y el frontend. Es decir, el servidor está enviando el HTML actualizado y el navegador lo está renderizando correctamente.

## Entregable

La tarea se considera completa si puedes demostrar estas cuatro cosas:

1. El entorno virtual esta creado y activado.
2. Las dependencias se instalaron desde `requirements.txt`.
3. La aplicacion corre en tu maquina y responde en el navegador.
4. Modificaste `templates/index.html` y podes señalar exactamente donde se refleja ese cambio.

## Cierre

No estas aprendiendo a tipear comandos. Estas empezando a construir criterio tecnico. Si hoy entiendes que levanta el servidor, de donde salen las dependencias y por que Flask encuentra esa plantilla, entonces arrancaste bien. Simple no significa superficial.
