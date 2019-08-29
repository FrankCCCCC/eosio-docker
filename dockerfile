FROM ubuntu
RUN apt-get update && apt-get install -y vim nano zsh curl git sudo wget g++ python3.6 nodejs npm

RUN mkdir eos
COPY eosio_1.7.0-1-ubuntu-18.04_amd64.deb /eos
WORKDIR /eos
RUN sudo apt install -y ./eosio_1.7.0-1-ubuntu-18.04_amd64.deb

RUN mkdir /eos/contracts
WORKDIR /eos/contracts
COPY eosio.cdt_1.6.1-1_amd64.deb /eos/contracts
RUN sudo apt install -y ./eosio.cdt_1.6.1-1_amd64.deb

RUN mkdir hello
COPY init.py /eos/contracts
COPY init1.py /eos/contracts
COPY hello.cpp /eos/contracts/hello

RUN keosd &
RUN nodeos -e -p eosio --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --access-control-allow-origin='*' --contracts-console --http-validate-host=false --verbose-http-errors >> nodeos.log 2>&1 &
# RUN curl http://localhost:8888/v1/chain/get_info
# RUN python3.6 readPassword.py
# RUN cleos wallet open -n docker_eos_default
# RUN cleos wallet list
# RUN cleos get account bob
