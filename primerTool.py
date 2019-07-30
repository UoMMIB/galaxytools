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


def arguments():
    parser = argparse.ArgumentParser(description='Read list of primers and output primer plate. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('-iceServer', default="http://ice.synbiochem.co.uk",
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
    with open (args.output,'w') as handler:
        csv.writer(handler).writerow(args.iceUser)
        
