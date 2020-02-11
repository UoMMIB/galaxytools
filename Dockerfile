FROM continuumio/miniconda3

RUN conda install numpy
RUN conda install pandas
RUN conda install scipy
RUN conda install xlrd

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