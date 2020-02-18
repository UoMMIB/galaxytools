#!/bin/bash
# Start Galaxy
docker run -it -v ${PWD}:/tools -v ${PWD}/data:/data -p 80:80 -e PLASMID_GENIE_PATH=/tools/code/PlasmidGenieClient -e DATA=/data -e ICE_SERVER=$ICE_SERVER -e ICE_USERNAME=$ICE_USERNAME -e ICE_PASSWORD=$ICE_PASSWORD sbc1 sh /tools/plasmidgenie_test.sh

#docker run -d -p 8080:80 -p 8021:21 -p 8022:22 -v ${PWD}/local_tools:/local_tools -v /var/run/docker.sock:/var/run/docker.sock -e GALAXY_CONFIG_TOOL_CONFIG_FILE=/local_tools/local_tools.xml,config/tool_conf.xml.sample sbcglx
