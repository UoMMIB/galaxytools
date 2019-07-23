#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:29:08 2019

@author: Pablo Carbonell, SYNBIOCHEM
@description: Get plate from primer list.
"""
import argparse
import pandas as pd
import csv
import os

def readPlate(df):
    well = {}
    wp = 'Well Position'
    sn = 'Sequence Name'
    try: 
        wp in df.columns and sn in df.columns
    except:
        raise Exception('Unknown columns')
    for ix in df.index:
        pos = df.loc[ix,'Well Position']
        seq = df.loc[ix,'Sequence Name']
        part = seq.split('_')[0]
        well[ pos ] = part
    return well

def makePlate(well, outfile):
    with open(outfile,'w') as h:
        cw = csv.writer( h )
        cw.writerow( ['well','id'] )
        for col in sorted( well ):
            cw.writerow( [col,well[col]+'_P'] )
    return
        

def arguments():
    parser = argparse.ArgumentParser(description='Read list of primers and output primer plate. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('infile', 
                        help='Input csv file.')
    parser.add_argument('outfile', 
                        help='Output csv file.')
    return parser

if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    if os.path.exists(arg.infile):
        try:
            df = pd.read_csv(arg.infile)
        except:
            raise Exception('Unkown file format!')
        well = readPlate(df)
        makePlate(well,arg.outfile)
    else:
        raise Exception('File not found')
        
