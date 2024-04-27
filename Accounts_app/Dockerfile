FROM public.ecr.aws/docker/library/python:slim-bullseye
LABEL authors="hadi"

WORKDIR src

COPY ./src /src
COPY ./requirments /requirments
RUN pip install -r /requirments/requirments.txt