# Use debian
From debian:stretch

# set version label
LABEL build_version="Debian-DDClient"
LABEL maintainer="popweasel"

# update the OS
RUN echo "*** Updating OS ***" \
    && DEBIAN_FRONTEND=noninteractive apt-get -q update \
    && echo "*** Installing ddclient and certificates ***" \
    && DEBIAN_FRONTEND=noninteractive apt-get -qy install ddclient \
        ca-certificates python3 \
    && rm -rf /var/lib/apt/lists/*

# ENTRYPOINT []
