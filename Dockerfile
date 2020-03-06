FROM cloudacademydevops/ide:python37
USER root
WORKDIR /root/lab/
COPY src ./src
COPY test ./test
