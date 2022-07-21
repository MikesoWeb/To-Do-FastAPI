import os
import uvicorn
from todo.main import app
if __name__ == '__main__':
    uvicorn.run("run:app", host="0.0.0.0", port=int(os.getenv("PORT", default=5000)),)
