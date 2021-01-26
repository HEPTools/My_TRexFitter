#!/bin/bash

cd low_mass_sys
find . -maxdepth 1 -type d -name "m*" -print0 | while read -d $'\0' file; do
    cd $file
    source fit_all.sh > /dev/null 2>&1 &
    cd ..
done
cd ..
