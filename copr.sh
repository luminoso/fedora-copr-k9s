#!/bin/sh

GITHUB_API_LATEST_VERSION=$(curl https://api.github.com/repos/derailed/k9s/releases/latest | jq -r ".tag_name")
echo "Latest tag: $GITHUB_API_LATEST_VERSION"

# remove "v" prefix
K9S_VERSION=${GITHUB_API_LATEST_VERSION#v}
echo "Version to build: ${K9S_VERSION}"

curl -O https://raw.githubusercontent.com/luminoso/fedora-copr-k9s/main/k9s.spec
sed -i "s/Version:        .*/Version:        ${K9S_VERSION}/g" k9s.spec
