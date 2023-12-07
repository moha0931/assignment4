FROM python:3.9

WORKDIR /moha0931_assignment4

COPY . /moha0931_assignment4

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]