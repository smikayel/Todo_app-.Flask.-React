FROM python:3.11-alpine3.15
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN pip install pymysql
RUN pip install PyMySQL
EXPOSE 5000
CMD flask db upgrade && python app.py
