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
                with zipfile.Zipfile(p) as myzip:
                    zipfile.extractall(path=ppath)
            else:
                shutil.copy(p,ppath)

def configureTool(args):
    """ Configure a local LCR2 tool based on the template """
    template = os.path.join( os.path.dirname(  __file__), 'lcr2_job.sh' )
    if not os.path.exists( args.tempFolder ):
       os.makedirs( args.tempFolder )
    script = os.path.join( args.tempFolder, 'job.sh' )
    log = os.path.join( args.tempFolder, 'log.sh' )
    df = pd.read_csv(args.plasmids)
    icelist = [str(x) for x in df['ICE']]
    icelist = ' '.join( icelist )
    with open( template ) as hin, open( script, 'w' ) as hout:
        for line in hin:
            line = re.sub( '{{plasmids}}', icelist, line )
            line = re.sub( '{{path}}', args.tempFolder, line )
            hout.write( line )
    source = os.path.getenv('SBC_ASSEMBLY_PATH')
    target = args.tempFolder
    locaTool(source,target,args.plates)
    return script, log

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
    script, log = configureTool( args )
    logout = open(log, 'w')
    print('Running lcr2 script...')
    subprocess.call( "bash "+script, shell=True, stdout=logout, stderr=logout )
    print('Done.')
    os.chdir(os.path.join( os.getenv( 'SBC_ASSEMBLY_PATH' ), 'out' ))
    
