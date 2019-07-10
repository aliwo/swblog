#!/usr/bin/env bash
sudo add-apt-repository ppa:ethereum/ethereum
sudo apt update
sudo apt install ethereum

wget https://github.com/ethereum-mining/ethminer/releases/download/v0.17.1/ethminer-0.17.1-linux-x86_64.tar.gz
tar -xvzf ethminer-0.17.1-linux-x86_64.tar.gz

ethminer -U -P stratum2+tcp://username.workername:x@asia.ethash-hub.miningpoolhub.com:20535
