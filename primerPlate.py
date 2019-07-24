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
    sn2 = 'Name'
    try: 
        wp in df.columns and (sn in df.columns or sn2 in df.columns)
    except:
        raise Exception('Unknown columns')
    for ix in df.index:
        pos = df.loc[ix,wp]
        try:
            seq = df.loc[ix,sn]
        except:
            seq = df.loc[ix,sn2]
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
    parser.add_argument('-i', '--input', action='append', 
                        help='Input csv file.')
    parser.add_argument('-o', '--output', 
                        help='Output csv file.')
    return parser

if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    for infile in args.i:
        if os.path.exists(infile):
            try:
                df = pd.read_csv(infile)
            except:
                raise Exception('Unkown file format!')
            well = readPlate(df)
            makePlate(well,args.o)
        else:
            raise Exception('File not found')
        
