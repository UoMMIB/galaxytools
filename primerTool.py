#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:29:08 2019

@author: Pablo Carbonell, SYNBIOCHEM
@description: Run the primer generation.
"""
import argparse
import pandas as pd
import csv
import os
import re
import subprocess
import shutil

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
    return parser

if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    os.chdir(os.path.join( os.path.dirname(__file__), 'sbc-assembly') )
    cmd = ["python", 'assembly/app/lcr2/primers.py', args.iceServer, args.iceUser,
           args.icePass, args.enzymes, args.temp]
    if args.plate is not None:
        cmd.append( args.plate )
    else:
        cmd.append( 'None' )
    df = pd.read_csv(args.plasmids)
    icelist = [str(x) for x in df['ICE']]
    icelist = [icelist[0]]
    for ice in icelist:
        cmd.append( ice )
    subprocess.call( cmd )
    outfile1 = 'primer_1_primer_phospho.csv'
    outfile2 = 'primer_1_primer_nonphospho.csv'
    if os.path.exists( outfile1 ):
        shutil.copyfile( outfile1, args.output )
        os.unlink( outfile1 )
    if os.path.exists( outfile2 ):
        os.unlink( outfile2 )
    os.chdir( '..' )
        
