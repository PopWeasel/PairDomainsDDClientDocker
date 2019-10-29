# PairDomainsDDClientDocker
Docker container using ddclient to update dynamic dns for domains hosted by pairdomains

## Create docker image

docker build -t ddclient:1 .

## Run docker inmage

docker run --rm --name roadsidepoppies-dns  -t ddclient:1 -p ${PAIR_DNS_KEY} -d roadsidepoppies.com -t 600
