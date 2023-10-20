FROM python:3.12.0b1-slim

WORKDIR /app

COPY console_calculator.py .

RUN rm -rf /root/.cache /var/cache /var/lib

CMD ["python3","console_calculator.py"]


