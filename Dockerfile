FROM python:3.6
WORKDIR /

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

# CMD ["gunicorn", "start:app", "-c", "./gunicorn.conf.py"]
CMD ["python3", "start.py"]