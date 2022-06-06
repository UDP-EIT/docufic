FROM python:3.8 AS build

RUN mkdir -p /opt/docufic

COPY . /opt/docufic/
WORKDIR /opt/docufic/

RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN python manage.py collectstatic

CMD gunicorn docufic.wsgi

FROM nginx

RUN mkdir /static

COPY --from=build /opt/docufic/static /static
COPY docufic.ensena.cl /etc/nginx/sites-available/
