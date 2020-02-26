#!/bin/bash
cd ${SBC_ASSEMBLY_PATH}
export PYTHONPATH=$PYTHONPATH:.
python ${SBC_ASSEMBLY_PATH}/assembly/app/lcr2/primers.py $ICE_SERVER $ICE_USERNAME $ICE_PASSWORD {{enzymes}} {{temp}} {{plates}} {{plasmids}}
