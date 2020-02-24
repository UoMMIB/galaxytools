#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:29:08 2019

@author: Pablo Carbonell, SYNBIOCHEM
@description: Run the primers generation.
"""
import argparse
import pandas as pd
import csv
import os
import re
import subprocess
import shutil
import zipfile
import glob
import tempfile
import shutil

def localTool(source,target,plates):
    """ LCR2 requires having in data/plates the appropriate plates
    for the current parts. Here the strategy is to copy the source
    code and replace data/plates with user's plates
    """
    shutil.copytree(source, target)
    if plates is not None:
        """ If plates is empty, take the default plates,
        otherwise, replace the plate files"""
        ppath = os.path.join(target,'data','plates')
        for p in glob.glob(os.path.join(ppath, '*')):
            os.unlink(p)
        for p in plates:
            if zipfile.is_zipfile(p):
                with zipfile.ZipFile(p) as myzip:
                    myzip.extractall(path=ppath)
            else:
                shutil.copy(p,ppath)
    """ Empty out folder """
    outdir = os.path.join(target,'out')
    shutil.rmtree(outdir)
    if not os.path.exists(outdir):
        os.mkdir(outdir)

def configureTool(args):
    """ Configure a local LCR2 tool based on the template """
    template = os.path.join( os.path.dirname(  __file__), 'lcr2_job.sh' )
    if args.tempFolder is None:
        tmpFolder = tempfile.mkdtemp()
    else:
        tmpFolder = args.tempFolder
    if not os.path.exists( tmpFolder ):
       os.makedirs( tmpFolder )
    script = os.path.join( tmpFolder, 'job.sh' )
    log = os.path.join( tmpFolder, 'log.sh' )
    df = pd.read_csv(args.plasmids)
    icelist = [str(x) for x in df['ICE']]
    icelist = ' '.join( icelist )
    source = os.getenv('SBC_ASSEMBLY_PATH')
    target = os.path.join( tmpFolder, os.path.basename(source) )
    with open( template ) as hin, open( script, 'w' ) as hout:
        for line in hin:
            line = re.sub( '{{plasmids}}', icelist, line )
            line = re.sub( '{{path}}', target, line )
            hout.write( line )
    localTool(source,target,args.plates)
    return script, log, target

# Zip the files from given directory that matches the filter
def zipFilesInDir(dirName, zipFileName):
    # create a ZipFile object
    with ZipFile(zipFileName, 'w') as zipObj:
        # Iterate over all the files in directory
        for folderName, subfolders, filenames in os.walk(dirName):
            for filename in filenames:
                # create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
                zipObj.write(filePath)

def arguments():
    parser = argparse.ArgumentParser(description='Work list generation for Ligase Cycling Reaction (LCR). Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('-iceServer', default=os.getenv('ICE_SERVER'),
                        help='ICE server url.')
    parser.add_argument('-iceUser', default=os.getenv('ICE_USERNAME'), 
                        help='ICE user.')
    parser.add_argument('-icePass', default=os.getenv('ICE_PASSWORD'),
                        help='ICE password.')
    parser.add_argument('-plasmids', 
                        help='Plasmid csv file.')
    parser.add_argument('-output', 
                        help='Output zip file.')
    parser.add_argument('-tempFolder',
                        help='Tool temporary folder.')
    parser.add_argument('-plates', action="append",
                        help='Plate files (csv or xlsx or zip).')    
    return parser

if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    # Fill out template and create a tmp copy of the code with the plates 
    script, log, target = configureTool( args )
    print(script)
    logout = open(log, 'w')
    print('Running lcr2 script...')
    subprocess.call( "bash "+script, shell=True, stdout=logout, stderr=logout )
    print('Done.')
    # Zip the contents of the "out" folder into the output file
    zipFilesInDir(os.path.join( os.path.dirname(target), 'out', args.output ))
