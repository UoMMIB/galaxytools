#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:29:08 2019

@author: Pablo Carbonell, SYNBIOCHEM
@description: Get plasmid info.
"""
import argparse
import os
import csv
import requests
from requests.auth import HTTPBasicAuth

def getSBCfileURL(f):
    host = os.getenv('SBCDATA_HOST')
    user = os.getenv('SBCDATA_USER')
    pwd = os.getenv('SBCDATA_PASSWORD')

    url = os.path.join(host, f)
    print('URL',url)
    r = requests.get(url, auth=HTTPBasicAuth(user,pwd))
    return r.text

def getSBCfileShared(f):
    shared = os.getenv('SBCDATA_SHARED')
    return open( os.path.join(shared, f) ).read()

def arguments():
    parser = argparse.ArgumentParser(description='Read list of primers and output primer plate. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('-i', '--input', action='append', 
                        help='Input csv file.')
    parser.add_argument('-o', '--output', 
                        help='Output csv file.')
    parser.add_argument('-r', '--remote', action='store_true',
                       help='Use URL access')
    return parser

if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    info = []
    for design in args.input:
        f = os.path.join('Designs', design, 'Design', design+'_export_mapping.csv')
        if args.remote:
            r = getSBCfileURL(f)
        else:
            r = getSBCfileShared(f)
        info.append( [row for row in csv.reader(r.split('\n'))] )
    with open( args.output, 'w') as h:
        cw = csv.writer(h)
        first = True
        for i in info:
            if first:
                cw.writerow(i[0])
                first = False
            for row in i[1:-1]:
                if len(row) > 1:
                    cw.writerow(row)
