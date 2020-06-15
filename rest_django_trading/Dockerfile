FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /manning/rest_django_trading
WORKDIR /manning/rest_django_trading
COPY requirements.txt /manning/rest_django_trading/
RUN pip install -r requirements.txt
ADD . /manning/rest_django_trading/

EXPOSE 8100

CMD ["gunicorn", "--chdir", "rest_django_trading", "--bind", ":8100", "rest_django_trading.wsgi:application"]