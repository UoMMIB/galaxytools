#!/bin/bash
export PYTHONPATH=$PYTHONPATH:${PLASMID_GENIE_PATH};
cd ${PLASMID_GENIE_PATH};
/home/mibsspc2/anaconda3/bin/python3 ${PLASMID_GENIE_PATH}/plasmid_genie/client.py $ICE_SERVER $ICE_USERNAME $ICE_PASSWORD synbiochem {{design}} {{output}} {{enzymes}}
