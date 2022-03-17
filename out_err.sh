#!/bin/bash

echoerr() { echo "$@" 1>&2; }

for i in {1..10}; do
    echo "[$i] Hello from stdout!"
    echoerr "[$i] Hello from stderr..."
    echoerr "[$i] second hello from stderr"
done
