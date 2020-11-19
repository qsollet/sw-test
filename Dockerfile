FROM python:3.8-slim

LABEL maintainer=quentin@sollet.fr

RUN useradd --create-home --shell /bin/bash appuser
USER appuser
ENV PATH="/home/appuser/.local/bin:${PATH}"

ENV GUNICORN_BIND_IP 0.0.0.0
ENV GUNICORN_BIND_PORT 8080
ENV GUNICORN_WORKER 4

COPY ./*.py /home/appuser/src/
COPY ./requirements.txt /home/appuser/src/
COPY ./run.sh /home/appuser/src/
WORKDIR /home/appuser/src
RUN pip install --user gunicorn psycopg2-binary && pip install --user -r requirements.txt

ENTRYPOINT ["./run.sh"]
