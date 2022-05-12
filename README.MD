Простой ToDo менеджер, реализованный на веб-фреймворке FastAPI В качестве веб-интерфейса использован фреймворк Semantic
UI https://semantic-ui.com/

Создаем папку для нового проекта и переходим в нее

    md ToDoFastAPI & cd ToDoFastAPI


Структура файлов и папок

    mkdir templates\todo
    mkdir static\css
    echo .> static/css/style.css
    echo .> .gitignore
    echo .> README.MD
    echo .> run.py
    md todo
    echo .> todo/__init__.py
    echo .> todo/database.py
    echo .> todo/models.py
    echo .> todo/views.py
    echo .> templates/todo/layout.html
    echo .> templates/todo/index.html 


Устанавливаем и активируем виртуальное окружение

    python3 -m venv venv
    . venv/bin/activate


Инициализируем git

    git init


Устанавливаем модули

    pip install fastapi uvicorn sqlalchemy jinja2
    pip install python-multipart


Или установить полный fastapi, включающий jinja2, python-multipart, uvicorn
    
    pip install fastapi[all] sqlalchemy


Создаем файл с зависимостями проекта

    pip freeze > requirements.txt


База данных должна быть в файле .gitignore, но для этого примера я ее оттуда удалил, чтобы был пример ToDo задач


Запускаем приложение

    uvicorn run:app --reload --port 5000


Ссылка на оригинал: https://youtu.be/3vfum74ggHE

    Терехов Михаил 2022 год