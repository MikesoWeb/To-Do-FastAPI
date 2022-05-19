from fastapi import Depends, Request, Form, status
from fastapi import FastAPI
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from todo.config import get_settings, Settings
from todo.database import SessionLocal
from todo.models import ToDo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')


# Создаем локальную сессию к базе данных
def get_db():
    # Каждый экземпляр класса SessionLocal будет сеансом базы данных
    db_session_local = SessionLocal()
    try:
        yield db_session_local
    finally:
        db_session_local.close()


@app.get('/')
def home(request: Request, settings: Settings = Depends(get_settings), db_session: Session = Depends(get_db),
         skip: int = 0, limit: int = 10):
    todos = db_session.query(ToDo).offset(skip).limit(limit).all()
    return templates.TemplateResponse('todo/index.html',
                                      {'request': request, 'todo_list': todos,
                                       'app_name': settings['app_name'],
                                       'title': 'ToDo менеджер'})


@app.post('/add')
def add(request: Request, title: str = Form(...), db_session: Session = Depends(get_db)):
    new_todo = ToDo(title=title)
    db_session.add(new_todo)
    db_session.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get('/update/{todo_id}')
def update(request: Request, todo_id: int, db_session: Session = Depends(get_db)):
    todo = db_session.query(ToDo).filter(ToDo.id == todo_id).first()
    todo.is_complete = not todo.is_complete
    db_session.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@app.get('/delete/{todo_id}')
def delete(request: Request, todo_id: int, db_session: Session = Depends(get_db)):
    todo = db_session.query(ToDo).filter(ToDo.id == todo_id).first()
    db_session.delete(todo)
    db_session.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
