FROM python:3.10

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry && poetry config virtualenvs.create false && poetry install --no-root --no-directory

COPY app/ app/
COPY setup.py .

CMD ["python", "./setup.py"]
