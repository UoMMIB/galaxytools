FROM continuumio/miniconda3

RUN conda install python=3.6.8
RUN conda install numpy
RUN conda install pandas
RUN conda install scipy
RUN conda install ipython
RUN conda install xlrd
RUN conda install -c omnia svgwrite
RUN conda install -c r rpy2
RUN conda install -c conda-forge r-r.utils 
RUN conda install gmp
RUN apt-get install libgmp-dev -y
RUN conda install -c conda-forge r-gmp 

RUN R -e "install.packages(c('partitions','DoE.base','crossdes','planor'), dependencies=TRUE, repos='https://cran.r-project.org', verbose=FALSE)"

RUN conda install reportlab
RUN conda install -c conda-forge svglib

RUN conda install six=1.10.0
RUN conda install -c conda-forge sseclient=0.0.22
RUN pip install synbiochem-py==0.6.18

RUN conda install -c anaconda biopython
RUN conda install -c bioconda blast

RUN mkdir /code
WORKDIR /code
RUN git clone https://gitlab+deploy-token-2:cyFxC4ogMcKih6Ls97Uj@gitlab.cs.man.ac.uk/SYNBIOCHEM/sbc-doe.git
WORKDIR /code/sbc-doe 
RUN git clone https://github.com/pablocarb/doebase.git

RUN mkdir /data 

WORKDIR /code

# Build the image:
# docker build -t sbc1 .
# Running Design2DoETool (doe2jmp):
# docker run -v ${PWD}/data/:/data/ sbc1 python /code/sbc-doe/doe2jmp.py -r -e -t -input /data/DoE_template.xlsx -o /data/output.txt 48