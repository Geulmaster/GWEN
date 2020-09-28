FROM python:3
WORKDIR /usr/src/GWEN
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "index.py"]