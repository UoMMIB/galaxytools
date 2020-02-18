#!/bin/bash
export PYTHONPATH=$PYTHONPATH:${PLASMID_GENIE_PATH};
cd ${PLASMID_GENIE_PATH};
python ${PLASMID_GENIE_PATH}/plasmid_genie/client.py $ICE_SERVER $ICE_USERNAME $ICE_PASSWORD synbiochem /data/plasmidgenie_in.dat plasmidgenie_out.zip MlyI
