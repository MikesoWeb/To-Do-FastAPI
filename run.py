import uvicorn
from todo.main import app
from todo.config import settings

if __name__ == '__main__':
    uvicorn.run("run:app", host="0.0.0.0", port=int(settings.port), log_level='info')
