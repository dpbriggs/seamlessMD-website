FROM python:3.6

RUN pip install -q flask redis
RUN mkdir ./templates
COPY main.py .
COPY patient_data_fixed.json .
COPY templates/main.html ./templates/main.html

CMD python main.py

EXPOSE 8080
