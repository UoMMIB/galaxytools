docker run -e "GALAXY_SLOTS=$GALAXY_SLOTS" --name c770324213d74b95898238582235ad62 -v /galaxy-central:/galaxy-central:ro -v /local_tools/galaxytools:/local_tools/galaxytools:ro -v /export/galaxy-central/database/job_working_directory/000/5:/export/galaxy-central/database/job_working_directory/000/5:ro -v /export/galaxy-central/database/job_working_directory/000/5/working:/export/galaxy-central/database/job_working_directory/000/5/working:rw -v /export/galaxy-central/database/files:/export/galaxy-central/database/files:rw -w /export/galaxy-central/database/job_working_directory/000/5/working --rm --user 1450:1450 sbc1 /bin/sh /export/galaxy-central/database/job_working_directory/000/5/tool_script.sh > ../tool_stdout 2> ../tool_stderr;

return_code=$?;

if [ -f /export/galaxy-central/database/job_working_directory/000/5/working/out1.jsl ] ; then
    cp /export/galaxy-central/database/job_working_directory/000/5/working/out1.jsl /export/galaxy-central/database/files/000/dataset_5.dat ;
fi;

cd '/export/galaxy-central/database/job_working_directory/000/5'; 
