#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
  echo 'USAGE: ./get.sh <Firewall Sentry URL> <Firewall Sentry Token>
  e.g., ./update.sh https://firewall.sentry XXYYZZ'
else
  curl $1 --header "FS-TOKEN: $2"
fi