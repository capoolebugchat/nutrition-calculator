from python:3.7-slim
copy . .
run pip install -r requirements.txt
CMD exec gunicorn --bind --port 80 --workers 1 --threads 8 --timeout 0 main:app