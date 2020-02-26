FROM python:3.6-alpine
RUN apk add --update make
WORKDIR /root/lab/
COPY src ./src
COPY test ./test
