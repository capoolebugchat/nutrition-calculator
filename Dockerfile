from python:3.7-slim
copy . .
run pip install -r requirements.txt
cmd ["python3" "server.py"]