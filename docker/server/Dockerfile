FROM python:3.9-slim

ENV PATH "${PATH}:/home/pythonuser/.local/bin"

COPY src/requirements.txt /tmp/

RUN apt-get update && apt-get -y install gcc python3-dev libpq-dev

RUN useradd --create-home pythonuser
USER pythonuser
WORKDIR /home/pythonuser/app

RUN pip install -r /tmp/requirements.txt

CMD [ "tail", "-f", "/dev/null" ]