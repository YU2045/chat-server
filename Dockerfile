FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /server

COPY ./ /server
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
EXPOSE 8000
# uvicornのサーバーを立ち上げる
CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--reload"]
