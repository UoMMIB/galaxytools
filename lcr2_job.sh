#!/bin/bash
export SBC_ASSEMBLY_PATH={{path}}
export PYTHONPATH=$PYTHONPATH:${SBC_ASSEMBLY_PATH};
cd ${SBC_ASSEMBLY_PATH}; 
python ${SBC_ASSEMBLY_PATH}/assembly/app/lcr2/lcr2_pipeline.py $ICE_SERVER $ICE_USERNAME $ICE_PASSWORD LCR True {{plasmids}}
