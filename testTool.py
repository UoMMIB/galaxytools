#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:29:08 2019

@author: Pablo Carbonell, SYNBIOCHEM
@description: Test tool.
"""
import argparse
import requests
import os

def outHTML(outFile):
    output = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Example</title>
    </head>
    <body>
        <p>This is an example of a simple HTML page with one paragraph.</p>
        An <img src="sbc.png">image</img>.
    </body>
    </html>
    """
    with open(outFile,'w') as h:
        h.write(output)
    
    r = requests.get('https://pbs.twimg.com/profile_images/607846881331412992/stXUAIwe_400x400.png')
    outfig = os.path.join( os.path.dirname(outFile), 'sbc.png') 
    open(outfig,'wb').write(r.content)
        
    


def arguments():
    parser = argparse.ArgumentParser(description='Read list of primers and output primer plate. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('-o', '--output', 
                        help='Output file.')
    return parser

if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    outHTML(args.output)
