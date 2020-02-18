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
    template = os.path.join( os.path.dirname(  __file__), 'plasmidgenie.sh' )
    if not os.path.exists( args.tempFolder ):
       os.makedirs( args.tempFolder )
    script = os.path.join( args.tempFolder, 'job.sh' )
    log = os.path.join( args.tempFolder, 'log.sh' )
    with open( template ) as hin, open( script, 'w' ) as hout:
        for line in hin:
            line = re.sub( '{{design}}', args.input, line )
            line = re.sub( '{{output}}', args.output, line )
            line = re.sub( '{{enzymes}}', args.enzymes, line )
            hout.write( line )
    return script, log

def arguments():
    parser = argparse.ArgumentParser(description='Work list generation for Ligase Cycling Reaction (LCR). Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('-iceServer', default=os.getenv('ICE_SERVER'),
                        help='ICE server url.')
    parser.add_argument('-iceUser', default=os.getenv('ICE_USERNAME'), 
                        help='ICE user.')
    parser.add_argument('-icePass', default=os.getenv('ICE_PASSWORD'),
                        help='ICE password.')
    parser.add_argument('-input', 
                        help='Combinatorial library txt file.')
    parser.add_argument('-output', 
                        help='Output zip file.')
    parser.add_argument('-enzymes',
                        help='Comma separated restriction enzymes.')
    parser.add_argument('-tempFolder',
                        help='Tool temporary folder.')
    return parser

if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    script, log = configureTool( args )
    print(script)
    logout = open(log, 'w')
    print('Running plasmid script...')
    subprocess.call( "bash "+script, shell=True, stdout=logout, stderr=logout )
    print('Done.')

    
