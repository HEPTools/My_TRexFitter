#!/bin/bash

cd high_mass_sys


cd m_42_mz2
source fit_all.sh *p80*.config > /dev/null 2>&1 &
cd ..

cd m_45
source fit_all.sh *p70*.config > /dev/null 2>&1 &
cd ..

cd m_48
source fit_all.sh *p70*.config > /dev/null 2>&1 &
cd ..

cd m_51
source fit_all.sh *p70*.config > /dev/null 2>&1 &
cd ..

cd m_54
source fit_all.sh *p70*.config > /dev/null 2>&1 &
cd ..

cd m_57
source fit_all.sh *p70*.config > /dev/null 2>&1 &
cd ..

cd m_60
source fit_all.sh *p60*.config > /dev/null 2>&1 &
cd ..

cd m_63
source fit_all.sh *p60*.config > /dev/null 2>&1 &
cd ..

cd m_66
source fit_all.sh *p60*.config > /dev/null 2>&1 &
cd ..

cd m_69
source fit_all.sh *p70*.config > /dev/null 2>&1 &
cd ..

cd m_72
source fit_all.sh *p70*.config > /dev/null 2>&1 &
cd ..

cd m_75
source fit_all.sh *p70*.config > /dev/null 2>&1 &
cd ..


cd ..
