# bigschool-taskmanager

Proyecto de gestión de tareas en consola desarrollado dentro del Máster en Desarrollo con IA de BigSchool. La aplicación permite crear, listar, completar y eliminar tareas de forma sencilla, y además incluye una funcionalidad opcional de IA para desglosar tareas complejas en subtareas más pequeñas y ejecutables.

## Descripción

Bigschool Task Manager es una pequeña aplicación de línea de comandos escrita en Python para gestionar listas de trabajo personales o de estudio. Está pensada como ejercicio práctico para trabajar con:

- programación Python
- gestión de archivos JSON
- variables de entorno
- integración con la API de OpenAI
- lógica de consola interactiva

## Funcionalidades

- Añadir tareas manualmente
- Listar todas las tareas almacenadas
- Marcar tareas como completadas
- Eliminar tareas
- Generar subtareas automáticamente a partir de una descripción compleja usando OpenAI
- Persistencia de datos en un archivo `tasks.json`

## Estructura del proyecto

- `main.py`: punto de entrada de la aplicación y menú interactivo
- `task_manager.py`: lógica de gestión de tareas y almacenamiento en JSON
- `ai_service.py`: integración con OpenAI para dividir tareas complejas en subtareas
- `test_task_manager.py`: pruebas unitarias para la lógica principal
- `requirements.txt`: dependencias del proyecto
- `.env`: archivo de configuración local para la clave API (no incluido en el repositorio)

## Requisitos

- Python 3.10 o superior
- Acceso a Internet para la funcionalidad con IA
- Clave API de OpenAI configurada en la variable de entorno `OPENAI_API_KEY`

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/javiescobar-dev/bigschool-taskmanager.git
   cd bigschool-taskmanager
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura la clave de la API de OpenAI en un archivo `.env`:

   ```env
   OPENAI_API_KEY=tu_clave_aqui
   ```

## Uso

Ejecuta la aplicación:

```bash
python main.py
```

### Menú principal

1. Añadir tarea
2. Añadir tarea compleja (con IA)
3. Listar tareas
4. Completar tarea
5. Eliminar tarea
6. Salir

### Ejemplo de flujo

- Crear una tarea simple como: `Estudiar Python`
- Crear una tarea compleja como: `Preparar una presentación del proyecto final`
- La IA la descompone en subtareas como:
  - Investigar contenido principal
  - Preparar estructura de la presentación
  - Crear diapositivas
  - Revisar y ajustar detalles

## Persistencia

Las tareas se guardan en un archivo local llamado `tasks.json` en la raíz del proyecto. Este archivo almacena cada tarea con:

- `id`
- `description`
- `completed`

## Integración con IA

La funcionalidad de IA está implementada en `ai_service.py` y utiliza la API de OpenAI para transformar una tarea compleja en varias subtareas más simples y accionables. Si la clave `OPENAI_API_KEY` no está configurada, la aplicación responde con un mensaje de error en lugar de intentar la llamada.

## Pruebas

El proyecto incluye pruebas unitarias para la lógica de tareas:

```bash
python -m unittest -q
```

## Objetivo del proyecto

Este repositorio sirve como una base práctica para aprender a combinar:

- Python orientado a consola
- gestión de datos con JSON
- interacción con APIs externas
- desarrollo de funcionalidades reales con un enfoque de producto mínimo viable

## Estado

Proyecto en desarrollo académico, con una base funcional para gestión de tareas y expansión posible con nuevas funcionalidades como:

- prioridad de tareas
- categorías
- fechas de vencimiento
- edición de tareas
- interfaz gráfica
- almacenamiento en base de datos
