#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:29:08 2019

@author: Pablo Carbonell, SYNBIOCHEM
@description: Postprocessing after running design2doe.
"""
import argparse
import os
import shutil
import zipfile
import glob


def arguments():
    parser = argparse.ArgumentParser(description='Postprocessing after running design2doe. Pablo Carbonell, SYNBIOCHEM, 2020')
    parser.add_argument('input', help='Input design file.')
    parser.add_argument('name', help='Design name')
    parser.add_argument('output', help='Output diagram file')
    parser.add_argument('output2', help='Output zip file')
    return parser

if __name__ == '__main__':
    parser = arguments()
    arg = parser.parse_args()
    pdf = os.path.join(os.path.dirname(arg.input), arg.name + '.pdf')
    shutil.copy(pdf, arg.output)
    with zipfile.ZipFile(arg.output2, 'w') as myzip:
        for f in glob.glob(os.path.join(os.path.dirname(arg.input),'*')):
            myzip.write(f,arcname=os.path.basename(f))
