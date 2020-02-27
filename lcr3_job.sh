#!/bin/bash
export SBC_ASSEMBLY_PATH={{path}}
cd ${SBC_ASSEMBLY_PATH}

export PATH=$PATH:/opt/conda/blast
export PYTHONPATH=$PYTHONPATH:.

python assembly/app/lcr3/lcr3_pipeline.py {{plasmids}} $ICE_SERVER $ICE_USERNAME $ICE_PASSWORD out/lcr3/ out/lcr3/summary.txt
