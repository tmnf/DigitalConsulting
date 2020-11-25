@Echo off

echo "Activating venv..."
call "venv/Scripts/activate.bat" 
echo "venv activated"

if exist requirements.txt (
    echo "Installing dependencias..."
    pip install -r requirements.txt
    echo "Dependencies Installed "
) else (
    echo "Ficheiro requirements.txt em falta..."
    EXIT /b
)

echo "A iniciar servidor..."
python manage.py runserver

