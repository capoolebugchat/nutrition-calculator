from python:3.7-slim
copy . .
run pip install uvicorn
run pip install fastapi
run pip install starlette
run pip install gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app