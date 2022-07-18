# Task manager

## Tests & Deployment

### Aclaración importante
La variable SECRET_KEY dentro de `tasks_project/settings.py` **ABSOLUTAMENTE NO** deberia estar hardcoded en el archivo por implicancias de seguridad

Mas info para en : https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

Luego de bajarse el proyecto ejecutar el script `.bat` para el proceso de test&build del proyecto:
```powershell
& '.\test&build_app.bat'
```
***Si no se dispone de windows***, ejecutar a mano los comandos dentro del `.bat`

Para validar que se levanto ok el servidor, probar accediendo a `http://127.0.0.1:8080/`

## UI diseñada
El front solo consiste en JS,CSS Y HTML

Para acceder a pagina principal, ir a `http://127.0.0.1:8080/tasks_app/`

### Crear tareas
Para crear una tarea, de forma `obligatoria`, llenar los campos de "CONTENIDO" y "FECHA".

Luego seleccionar "Crear tarea"

Revisar que se confirmo la creacion de la tarea (tanto del lado del cliente como del servidor)

### Filtrar/buscar/mostrar tareas
- Para buscar/filtrar tareas simplemente completar los campos necesarios (2 inputs)

- En caso que no se quiera filtrar dejarlos vacios y dar directamente a buscar

- En caso querer sacar la tabla, seleccionar "Limpiar"

### Eliminar y completar tarea
- Con la tabla en pantalla, seleccionar el icoco de ❌ para eliminarla

- Con la tabla en pantalla, seleccionar el icoco de ✔️ para completarla. Volver a seleccionar "Filtrar/buscar" para ver los cambios del completado

### Aclaraciones
- Todas las operaciones se encuentran en un log para el servidor y algunas acciones del lado del cliente tambien se encuentran logueadas

- El log del servidor se pisa cada vez que se reinicia        
