FROM python

COPY main.py /python/

COPY rawdata/cities.txt /python/rawdata/
COPY rawdata/instagrammers.csv /python/rawdata/
COPY rawdata/productos.csv /python/rawdata/

COPY newtables/__init__.py /python/newtables/
COPY newtables/comp_mueble.py /python/newtables/
COPY newtables/composicion.py /python/newtables/
COPY newtables/ventas.py /python/newtables/

COPY rawtables/__init__.py /python/rawtables/
COPY rawtables/clientes.py /python/rawtables/
COPY rawtables/influencers.py /python/rawtables/
COPY rawtables/muebles.py /python/rawtables/

COPY requirements.txt /python/

WORKDIR /python/
RUN pip install -r requirements.txt


ENTRYPOINT ["python3", "main.py"]