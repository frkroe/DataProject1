FROM python

COPY main.py /python/
COPY ./rawdata/ /python/rawdata/
COPY ./newtables/ /python/newtables/
COPY ./rawtables/ /python/rawtables/
COPY ./tablas/ /python/tablas/
COPY requirements.txt /python/

WORKDIR /python/
RUN pip install -r requirements.txt


ENTRYPOINT ["python3", "main.py"]
