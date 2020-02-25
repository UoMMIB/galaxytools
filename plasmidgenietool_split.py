#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Feb 2020

@author: Pablo Carbonell, SYNBIOCHEM
@description: Extract the plasmidgenie files
"""
import pd
import argparse
import zipfile
import shutil

ef arguments():
    parser = argparse.ArgumentParser(description='Split Plasmif Genie output. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('--input',  
                        help='Input file.')
    parser.add_argument('--output1', 
                        help='Export csv file.')
    parser.add_argument('--output2', 
                        help='Export mapping csv file.')
    return parser

if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    os.basename(args.input)
    z = zipfile.ZipFile(args.input)
    for f in z.namelist():
        if f.endswith('_export.csv'):
            outpath = os.path.dirname(args.output1)
            z.extract(f,path=outpath)
            shutil.move(os.path.join(outpath,os.path.basename(f)), args.output1)
        elif f.endswith('_export_mapping.csv'):
            outpath = os.path.dirname(args.output2)
            z.extract(f,path=outpath)
            shutil.move(os.path.join(outpath,os.path.basename(f)), args.output2)
    os.unlink(args.input)
