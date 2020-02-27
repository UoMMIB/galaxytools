#!/bin/bash
export SBC_ASSEMBLY_PATH={{path}}
cd ${SBC_ASSEMBLY_PATH}
export PYTHONPATH=$PYTHONPATH:.
python assembly/app/lcr2/lcr2_pipeline.py $ICE_SERVER $ICE_USERNAME $ICE_PASSWORD LCR True {{plasmids}}
