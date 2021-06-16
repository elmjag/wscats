FROM continuumio/miniconda3:4.9.2

RUN conda install --channel conda-forge \
    python=3.8.6 \
    django=3.2.4 \
    pytango=9.3.3 \
    black=21.5b2 \
    pip=21.1.1

RUN pip install channels==3.0.3

RUN mkdir /app
WORKDIR /app
COPY pucks pucks/
COPY wscats wscats/
COPY manage.py ./
RUN ./manage.py migrate

CMD ["/app/manage.py", "runserver", "0.0.0.0:8000"]