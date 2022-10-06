#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
  echo 'USAGE: ./update.sh <Firewall Sentry URL> <Firewall Sentry Host (myself)> <Firewall Sentry Token>
  e.g., ./update.sh https://firewall.sentry laptop XXYYZZ'
else
  curl -X POST $1 --header "FS_HOST: $2" --header "FS_TOKEN: $3"
fi