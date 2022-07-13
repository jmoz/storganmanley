FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY . .

CMD python3 -m unittest anagrams.py && python3 anagrams.py