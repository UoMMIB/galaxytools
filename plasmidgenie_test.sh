#!/bin/bash
export PYTHONPATH=$PYTHONPATH:${PLASMID_GENIE_PATH};
cd ${PLASMID_GENIE_PATH};
python ${PLASMID_GENIE_PATH}/plasmid_genie/client.py $ICE_SERVER $ICE_USERNAME $ICE_PASSWORD synbiochem /data/plasmidgenie_in.dat plasmidgenie_out.zip MlyI

python plasmid_genie/client.py  https://ice.synbiochem.co.uk pablo.carbonell@manchester.ac.uk synbiochem2020 synbiochem  /local_tools/galaxytools/dataset_99.dat plasmidgenie_out.zip MlyI

cd /local_tools/galaxytools/code/PlasmidGenieClient; python plasmid_genie/client.py https://ice.synbiochem.co.uk pablo.carbonell__at__manchester.ac.uk synbiochem2020 synbiochem /export/galaxy-central/database/files/000/dataset_99.dat /export/galaxy-central/database/files/000/dataset_108.dat MlyI
