#!/usr/bin/env python3                                                                                                                 
# -*- coding: utf-8 -*-                                                                                                                
"""                                                                                                    
Created on Tue Mar 19 09:29:08 2019                                                                                             
@author: Pablo Carbonell, SYNBIOCHEM
@description: Convert ICE registries into an orderlist
"""
import argparse
import glob
import shutil
import re
import os
import csv
from Bio import SeqIO


def order(inputFile, outputFile):
    with open(inputFile, 'w') as out:
        cw = csv.writer(out)
        cw.writerow( ('ICE', 'Sequence') )
        raise Exception('Tool not finished')
# TO DO: extract the GenBank files from the zip file
        for f in sorted(glob.glob('data/*.gb')):
            L = 'LOCUS       PABLOFIXD     5028 bp    DNA             PLN       21-JUN-1999'
            line = 1
            f2 = f+'.fix'
            ice = re.sub('\.gb','',os.path.basename(f))
            with open(f) as h, open(f2, 'w') as h2:
                for row in h:
                    if line == 1:
                        h2.write(L+'\n')
                    else:
                        h2.write(row)
                    line += 1
            with open(f2, "rU") as input_handle:
                for record in SeqIO.parse(input_handle, "genbank"):
                    cw.writerow( (ice,record.seq) )


def arguments():
    parser = argparse.ArgumentParser(description='Convert ICE regitries into an order list. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('input',  help='Input ICE ids.')
    parser.add_argument('output',  help='Output table.')
    return parser

    
if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    order(args.input,args.output)
