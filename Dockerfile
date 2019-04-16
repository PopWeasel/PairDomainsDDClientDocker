# Use debian
From debian:stretch

# set version label
LABEL build_version="Debian-DDClient"
LABEL maintainer="popweasel"

# update the OS
RUN echo "*** Updating OS ***"
RUN DEBIAN_FRONTEND=noninteractive apt-get -q update
RUN echo "*** Installing ddclient and certificates ***"
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install ddclient ca-certificates \
    python3 git
# RUN rm -rf /var/lib/apt/lists/*

RUN mkdir ddclient
WORKDIR ddclient
COPY runDDClient.py .
ENTRYPOINT ["python3", "runDDClient.py"]
