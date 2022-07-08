from python:3.9-slim
copy . .
run python3 -m pip install json
run pip install -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app