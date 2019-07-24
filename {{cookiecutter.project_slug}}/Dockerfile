ARG BASE_CONTAINER=rockstat/band-base-py:3.7
FROM $BASE_CONTAINER

WORKDIR /usr/src/services

LABEL band.service.version="{{ cookiecutter.version }}"
LABEL band.service.title="{{ cookiecutter.project_title }}"
LABEL band.service.def_position="{{ cookiecutter.dashboard_position }}"

ENV HOST=0.0.0.0
ENV PORT=8080
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE ${PORT}
COPY . .

CMD [ "python", "-m", "{{cookiecutter.project_slug}}"]
