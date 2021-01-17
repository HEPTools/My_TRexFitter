#!/bin/bash

cd low_mass_sys


cd m_05
source fit_all.sh *p40*.config > /dev/null 2>&1 &
cd ..

cd m_07
source fit_all.sh *p30*.config > /dev/null 2>&1 &
cd ..

cd m_09
source fit_all.sh *p30*.config > /dev/null 2>&1 &
cd ..

cd m_11
source fit_all.sh *p30*.config > /dev/null 2>&1 &
cd ..

cd m_13
source fit_all.sh *p30*.config > /dev/null 2>&1 &
cd ..

cd m_15
source fit_all.sh *p30*.config > /dev/null 2>&1 &
cd ..

cd m_17
source fit_all.sh *p30*.config > /dev/null 2>&1 &
cd ..

cd m_19
source fit_all.sh *p30*.config > /dev/null 2>&1 &
cd ..

cd m_23
source fit_all.sh *p30*.config > /dev/null 2>&1 &
cd ..

cd m_27
source fit_all.sh *p40*.config > /dev/null 2>&1 &
cd ..

cd m_31
source fit_all.sh *p40*.config > /dev/null 2>&1 &
cd ..

cd m_35
source fit_all.sh *p30*.config > /dev/null 2>&1 &
cd ..

cd m_39
source fit_all.sh *p50*.config > /dev/null 2>&1 &
cd ..

cd ..
