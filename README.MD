Простой ToDo менеджер, реализованный на веб-фреймворке FastAPI
В качестве веб-интерфейса использован фреймворк Semantic UI https://semantic-ui.com/

Создаем папку для нового проекта и переходим в нее

    md ToDoFlask & cd ToDoFlask

Структура файлов и папок

    md templates
    mkdir static\css
    echo .> .gitignore
    echo .> README.MD
    echo .> app.py
    echo .> database.py
    echo .> models.py
    echo .> templates/layout.html
    echo .> templates/index.html
    echo .> static/css/style.css

Устанавливаем и активируем виртуальное окружение

    python3 -m venv venv
    . venv/bin/activate


Инициализируем git

    git init


Устанавливаем модули

    pip install fastapi uvicorn sqlalchemy jinja2
    pip install python-multipart


Создаем файл с зависимостями проекта

    pip freeze > requirements.txt

Запускаем приложение

    uvicorn app:app --reload

Ссылка на оригинал: https://youtu.be/3vfum74ggHE
    
    Терехов Михаил 2022 год