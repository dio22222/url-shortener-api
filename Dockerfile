FROM python:3.13-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/url-shortener-api
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
