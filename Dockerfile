FROM ubuntu
USER root

RUN apt-get update
RUN apt-get -y install locales build-essential python python3 git diffstat texinfo gawk chrpath wget cpio nano vim mc iptables lzop devscripts ca-certificates gnome-terminal libcanberra-gtk3-module nfs-common python-pip python3-pip
RUN pip3 install pandas numpy sklearn flask

WORKDIR /src

COPY . .

CMD python3 server.py