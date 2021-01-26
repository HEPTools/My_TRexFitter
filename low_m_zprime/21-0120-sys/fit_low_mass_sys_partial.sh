#!/bin/bash

cd low_mass_sys
find . -maxdepth 1 -type d -name "m*" -print0 | while read -d $'\0' file; do
    cd $file
    source fit_all.sh *p00*.config > /dev/null 2>&1 &
    source fit_all.sh *p30*.config > /dev/null 2>&1 &
    source fit_all.sh *p40*.config > /dev/null 2>&1 &
    source fit_all.sh *p50*.config > /dev/null 2>&1 &
    cd ..
done
cd ..
