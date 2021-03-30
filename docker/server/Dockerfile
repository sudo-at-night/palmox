FROM python:3.9-alpine

ENV PATH "${PATH}:/home/pythonuser/.local/bin"

COPY src/requirements.txt /tmp/

RUN adduser --disabled-password pythonuser
USER pythonuser
WORKDIR /home/pythonuser/app

RUN pip install -r /tmp/requirements.txt

CMD [ "tail", "-f", "/dev/null" ]