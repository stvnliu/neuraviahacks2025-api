FROM python:3.12
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./public/ /code/public/
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/app
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
