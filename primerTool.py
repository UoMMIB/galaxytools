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


def configureTool(args):
    template = os.path.join( os.path.dirname(  __file__), 'primers.sh' )
    if not os.path.exists( args.tempFolder ):
       os.makedirs( args.tempFolder )
    script = os.path.join( args.tempFolder, 'job.sh' )
    log = os.path.join( args.tempFolder, 'log.sh' )
    if args.plate is not None:
        plate = args.plate 
    else:
        plate =  'None' 
        df = pd.read_csv(args.plasmids)
    icelist = [str(x) for x in df['ICE']]
    icelist = ' '.join( [ icelist[0] ] )
    with open( template ) as hin, open( script, 'w' ) as hout:
        for line in hin:
            line = re.sub( '{{enzymes}}', args.enzymes, line )
            line = re.sub( '{{temp}}', args.temp, line )
            line = re.sub( '{{plates}}', plate, line )
            line = re.sub( '{{plasmids}}', icelist, line )
            hout.write( line )
    return script, log

def arguments():
    parser = argparse.ArgumentParser(description='Read list of primers and output primer plate. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('-iceServer', default=os.getenv('ICE_SERVER'),
                        help='ICE server url.')
    parser.add_argument('-iceUser', default=os.getenv('ICE_USERNAME'), 
                        help='ICE user.')
    parser.add_argument('-icePass', default=os.getenv('ICE_PASSWORD'),
                        help='ICE password.')
    parser.add_argument('-enzymes',  default="MlyI",
                        help='Comma separated restriction enzymes.')
    parser.add_argument('-temp',  default="60",
                        help='Melting temperature.')
    parser.add_argument('-plate', 
                        help='Existing plate.')
    parser.add_argument('-plasmids', 
                        help='Plasmid csv file.')
    parser.add_argument('-output', 
                        help='Output csv file.')
    parser.add_argument('-tempFolder',
                        help='Tool temporary folder.')
    return parser

if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    script, log = configureTool( args )
    logout = open(log, 'w')
    print('Running primers script...')
    subprocess.call( "bash "+script, shell=True, stdout=logout, stderr=logout )
    print('Done.')
    os.chdir(os.getenv( 'SBC_ASSEMBLY_PATH' ))
    outfile1 = 'primer_1_primer_phospho.csv'
    outfile2 = 'primer_1_primer_nonphospho.csv'
    if os.path.exists( outfile1 ):
        shutil.copyfile( outfile1, args.output )
        os.unlink( outfile1 )
    if os.path.exists( outfile2 ):
        os.unlink( outfile2 )
        
