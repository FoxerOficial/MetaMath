# MetaMath - Sistema de Gestión de Aprendizaje Electrónico

MetaMath es un sistema de gestión de aprendizaje y evaluación en línea para la educación académica.


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


Mis agradecimientos para las personas que me apoyaron tanto con el proyecto como emocionalmente <i class="bi bi-chevron-down"></i>
                </a>
            </strong>
            <div class="collapse mt-2" id="agradecimientosCollapse">
                <ul class="list-unstyled mb-0">
                    <li>• Jesucristo</li>
                    <li>• Juan Camilo Giraldo (Top analistas, en serio, gracias milo :D)</li>
                    <li>• Neaz Mahmud (Creador de ELMS-swe, Base)</li>
                    <li>• Brayandiazc (Aprendiendo JavaScript)</li>
                    <li>• Franlu (Programación y Lenguaje de Marcas)</li>
                    <li>• Enflujo (Programación Creativa)</li>
                    <li>• Datauy (Elijo Estudiar)</li>
                    <li>• Tareas Plus (Matemáticas y Física)</li>
                    <li>• Julio Profe (Matemáticas y Física)</li>
                    <li>• CrashCourse (Educación académica en múltiples disciplinas)</li>
                    <li>• Educatina (Videos educativos en diversas materias)</li>
                    <li>• Khan Academy (Recursos educativos gratuitos)</li>
                    <li>• SamuNoHDMI  (Gracias por esas sugerencias en febrero mano, de veras)</li>
                    <li>• Juan Carlos Jaramillo</li>
                    <li>• Torres</li>
                    <li>• Romero</li>
                    <li>• Stefany</li>
                    <li>• Daniel</li>
                    <li>• Saray</li>
                    <li>• Jorge David</li>
                    <li>• Toñiro</li>
                    <li>• Hurto Calificado (Hurtado)</li>
                    <li>• Alexandra Landázuri</li>
                    <li>• Uladislao Bravo</li>
                    <li>• Copilot (Microsoft)</li>
                    <li>• Copilot (GitHub)</li>
                    <li>• Y muchas personas más</li>
                </ul>
            </div>

            
> **Nota:** Este proyecto fue desarrollado de forma independiente tomando como base el proyecto [ELMS-Swe](https://github.com/nz-m/eLMS-SWE), adaptando y expandiendo sus funcionalidades para ajustarse a las necesidades de MetaMath.
