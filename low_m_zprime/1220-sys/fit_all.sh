#!/bin/bash

if
    [ -z "$1"]
then
    find . -name "*.config" -print0 | while read -d $'\0' file; do
        trex-fitter n ./$file
        trex-fitter d ./$file
        trex-fitter w ./$file
        trex-fitter f ./$file
        trex-fitter p ./$file
        trex-fitter l ./$file
    done
else
    trex-fitter n ./$1
    trex-fitter d ./$1
    trex-fitter w ./$1
    trex-fitter f ./$1
    trex-fitter p ./$1
    trex-fitter l ./$1
fi
