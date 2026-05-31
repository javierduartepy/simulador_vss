 simulador_vss/
├── .gitignore
├── .env
├── requirements.txt
├── README.md
└── src/
    ├── manage.py             <-- Único archivo suelto de arranque
    ├── static/
    ├── media/
    ├── templates/            <-- CARPETA INDEPENDIENTE (.html)
    │   ├── base.html
    │   ├── inicio.html
    │   ├── provider/
    │   ├── writer/
    │   └── service/
    │
    └── apps/                 <-- CINCO CARPETAS HERMANAS ADENTRO (.py)
        ├── core/             <-- 1. Configuraciones generales (Cero archivos sueltos)
        │   ├── __init__.py
        │   ├── settings.py   
        │   ├── urls.py       
        │   └── wsgi.py
        │
        ├── pages/            <-- 2. Conector .py de las vistas con los templates
        │   ├── __init__.py
        │   ├── app.py
        │   ├── views.py
        │   └── urls.py
        │
        ├── provider/         <-- 3. Módulo de Almacenamiento (TABLA_SNAPSHOTS)
        │   ├── migrations/
        │   ├── __init__.py
        │   ├── app.py
        │   ├── models.py
        │   └── ...
        │
        ├── writer/           <-- 4. Módulo de Aplicación (TABLA_DATOS)
        │   ├── migrations/
        │   ├── __init__.py
        │   ├── app.py
        │   ├── models.py
        │   └── ...
        │
        └── service/          <-- 5. Módulo del Coordinador Central (TABLA_VOLUMENES)
            ├── migrations/
            ├── __init__.py
            ├── app.py
            ├── models.py
            └── ...


mkdir simulador_vss

# Crear la carpeta principal del proyecto y entrar en ella
mkdir mi_proyecto_vss
cd mi_proyecto_vss

# Crear los archivos raíz externos
echo. > .gitignore
echo. > .env
echo. > requirements.txt
echo. > README.md

# Crear la carpeta src y sus directorios independientes de diseño
mkdir src
mkdir src\static
mkdir src\media
mkdir src\templates
mkdir src\templates\base
mkdir src\templates\inicio
mkdir src\templates\core_service
mkdir src\templates\writer
mkdir src\templates\provider

# Crear la carpeta de aplicaciones y tus cuatro carpetas hermanas
mkdir src\apps
mkdir src\apps\pages
mkdir src\apps\provider
mkdir src\apps\writer
mkdir src\apps\core_service


# Crear el entorno virtual (llamado env_vss)
python -m venv env_vss

# Activar el entorno virtual 
env_vss\Scripts\activate

django>=4.2,<5.0
psycopg2-binary>=2.9.0
python-dotenv>=1.0.0


git remote add origin https://github.com/javierduartepy/simulador_vss
