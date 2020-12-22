FROM ubuntu:latest

# Install OpenJDK 8
RUN \
    apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    rm -rf /var/lib/apt/lists/*

# Install Python
RUN apt-get update && apt-get install -y software-properties-common

RUN \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y curl python3.7 python3.7-dev python3.7-distutils python3-pip python3-virtualenv && \
    rm -rf /var/lib/apt/lists/*

# Register the version in alternatives
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1

# Set python 3 as the default python
RUN update-alternatives --set python /usr/bin/python3.7


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_FORMAT=legacy

RUN apt-get update -y && apt-get install -y libzbar-dev bash gcc git libc-dev curl wget vim nano
RUN apt-get update -y && apt-get install -y build-essential

RUN apt-get update -y && apt-get install -y ranger caca-utils highlight atool w3m poppler-utils mediainfo

RUN apt-get update && apt-get install -y iputils-ping telnet
RUN apt-get install -y netcat && apt-get autoremove -y
RUN apt-get update && apt-get clean

RUN apt-get update \
    && apt-get install unixodbc -y \
    && apt-get install unixodbc-dev -y \
    && apt-get install freetds-dev -y \
    && apt-get install freetds-bin -y \
    && apt-get install tdsodbc -y \
    && apt-get install --reinstall build-essential -y

# populate "ocbcinst.ini" as this is where ODBC driver config sits
RUN echo "[FreeTDS]\n\
    Description = FreeTDS Driver\n\
    Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
    Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

RUN useradd -m alireza && echo "alireza:alireza" | chpasswd && adduser alireza sudo

#Install Jupyter:
RUN pip3 install jupyterlab

COPY docker_jupyter/requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt \
    && rm -rf requirements.txt

RUN mkdir -p /notebooks

WORKDIR /notebooks
ADD ./notebooks ./

COPY docker_jupyter/jupyter_run.sh /jupyter_run.sh
RUN chmod +x /jupyter_run.sh
