# MetaMath - Sistema de Gestión de Aprendizaje Electrónico

MetaMath es un sistema de gestión de aprendizaje y evaluación en línea para la educación académica.

> **Nota:** Este proyecto fue desarrollado de forma independiente tomando como base el proyecto [ELMS-Swe](https://github.com/nz-m/eLMS-SWE), adaptando y expandiendo sus funcionalidades para ajustarse a las necesidades de MetaMath.

## Características

- El administrador añade cursos, profesores y estudiantes, y les asigna cursos.
- El profesor crea el contenido del curso, anuncios, tareas, exámenes, toma de asistencia, etc. Puede ver los detalles y el análisis de las evaluaciones.
- Los estudiantes pueden inscribirse en los cursos con la clave de acceso, ver el contenido de los cursos en los que están inscritos, participar en las evaluaciones y ver sus resultados en detalle.
- Sección de discusión para profesores y estudiantes.

## Esquema relacional

![esquema]("C:\Users\imthe\Downloads\esquema0102.png")

## Pila tecnológica

1. Django 4.0.4
2. Bootstrap 5.0.2
3. jQuery 3.6.0
4. Chart.js v3.9.1
5. Animate.css 4.1.1

## Ejecución local

1. Accede al directorio del proyecto

```bash
cd MetaMath
```

2. Crea un entorno virtual y actívalo (Windows)

```bash
python -m venv env
env\Scripts\activate
```

3. Instala las dependencias

```bash
pip install -r requirements.txt
```

> **Nota:** Si usas versiones más recientes de Python (3.10 o superior), puede que necesites agregar la opción `--use-deprecated=legacy-resolver` al instalar dependencias con `pip` para evitar errores:

```bash
pip install -r requirements.txt --use-deprecated=legacy-resolver
```

4. Realiza las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crea el administrador/superusuario

```bash
python manage.py createsuperuser
```

6. Finalmente, ejecuta el proyecto

```bash
python manage.py runserver
```

Ahora el proyecto debería estar ejecutándose en http://127.0.0.1:8000/

Inicia sesión como administrador y añade algunos cursos, profesores y estudiantes.

## Licencia

[Licencia MIT (MIT)](https://github.com/nz-m/eLMS-SWE/blob/main/LICENCE)