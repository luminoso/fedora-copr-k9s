#!/bin/sh
wget https://raw.githubusercontent.com/luminoso/fedora-copr-k9s/main/k9s.spec
wget https://raw.githubusercontent.com/derailed/k9s/master/Makefile

VERSION=$(grep -Po "[0-9]+\.[0-9]+\.[0-9]+$" Makefile)
echo "Version to build: ${VERSION}"
sed -i "s/Version:        .*/Version:        ${VERSION}/g" k9s.spec

