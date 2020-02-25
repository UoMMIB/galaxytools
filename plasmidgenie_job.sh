#!/bin/bash
export PYTHONPATH=$PYTHONPATH:${PLASMID_GENIE_PATH};
cd ${PLASMID_GENIE_PATH};
export PG_OUTPUT=/tmp/output.zip
python ${PLASMID_GENIE_PATH}/plasmid_genie/client.py $ICE_SERVER $ICE_USERNAME $ICE_PASSWORD $ICE_GROUP $INPUT $PG_OUTPUT MlyI 
python /tools/plasmidgenietool_split.py --input $PG_OUTPUT --output1 $OUTPUT1 --output2 $OUTPUT2
