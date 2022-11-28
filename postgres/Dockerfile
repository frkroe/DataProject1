FROM python

COPY main.py /postgres/
COPY tablas/__init__.py /postgres/tablas/
COPY tablas/crear_tablas.py /postgres/tablas/
COPY tablas/alimentar_tablas.py /postgres/tablas/

COPY requirements.txt /postgres/

WORKDIR /postgres/
RUN pip install -r requirements.txt


ENTRYPOINT ["python3", "main.py"]