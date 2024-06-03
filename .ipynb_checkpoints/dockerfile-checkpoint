FROM python:3.9.19-bookworm
ENV PYTHONUNBUFFERED=1
WORKDIR /volumetest

COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir credentials

COPY . .

VOLUME /credentials

CMD [ "python3", "-m", "volumetest"]