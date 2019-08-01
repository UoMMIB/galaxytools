#!/bin/bash
export PYTHONPATH=$PYTHONPATH:${SBC_ASSEMBLY_PATH};
cd ${SBC_ASSEMBLY_PATH}; 
/home/mibsspc2/anaconda3/bin/python3 ${SBC_ASSEMBLY_PATH}/assembly/app/lcr2/primers.py $ICE_SERVER $ICE_USERNAME $ICE_PASSWORD {{enzymes} {{temp}} {{plates}} {{plasmids}}
