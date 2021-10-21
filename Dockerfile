FROM ubuntu:18.04
RUN (apt update && \
    apt list --upgradable && \
    apt-get install -y wget openssl linux-libc-dev ca-certificates apt-transport-https libssl1.0.0 python3 python3-distutils python3-pip locales && \
    apt-get autoremove) || exit 1
WORKDIR /opt/bits/auth
COPY . /opt/bits/auth
RUN pip3 install -r requirement.txt
# RUN update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8 
ENV LANGUAGE=en_US.en
ENV LC_ALL=en_US.UTF-8
ENV MONGO_URI=0.0.0.0:27017
RUN echo LANG=en_US.UTF-8 >> /etc/environment
RUN cat /etc/environment
EXPOSE 5001:5001 27017:27017
CMD ["python3", "app.py"]
