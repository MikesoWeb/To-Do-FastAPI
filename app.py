from fastapi import FastAPI, Depends, Request, Form, status
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory='templates')
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(models.ToDo).all()
    return templates.TemplateResponse('index.html',
                                      {'request': request, 'todo_list': todos, 'title': 'Главная страница'})


@app.post('/add')
def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = models.ToDo(title=title)
    db.add(new_todo)
    db.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get('/update/{todo_id}')
def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    todo.is_complete = not todo.is_complete
    db.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@app.get('/delete{todo_id}')
def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.ToDo).filter(models.ToDo == todo_id).first()
    db.delete(todo)
    db.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
