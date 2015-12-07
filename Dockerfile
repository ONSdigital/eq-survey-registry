FROM python:2.7.10

RUN mkdir /opt/eq-survey-registry
ADD ./requirements.txt /opt/eq-survey-registry/requirements.txt
RUN pip install -r /opt/eq-survey-registry/requirements.txt
ADD . /opt/eq-survey-registry
WORKDIR /opt/eq-survey-registry
EXPOSE 8081

WORKDIR /opt/eq-survey-registry
ENTRYPOINT python eq_couch.py && gunicorn -w 4 -b 0.0.0.0:8081 --config=gunicorn.py survey_registry:app
