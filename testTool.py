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

def outHTML(outFile, outPath):

    outfigname = 'sbc.png'
    outfig = os.path.join( outPath, outfigname )
    output = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Example</title>
    </head>
    <body>
        <p>This is an example of a simple HTML page with one paragraph.</p>
        <div>An image:<img src="{}" width="100px"></img>.</didv>
    </body>
    </html>
    """.format( outfigname )


    with open(outFile,'w') as h:
        h.write(output)
    
    if not os.path.exists(outPath):
       os.makedirs( outPath )
    r = requests.get('https://pbs.twimg.com/profile_images/607846881331412992/stXUAIwe_400x400.png')

    open(outfig,'wb').write(r.content)
        
    


def arguments():
    parser = argparse.ArgumentParser(description='Read list of primers and output primer plate. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('-o', '--output', 
                        help='Output file.')
    parser.add_argument('-p', '--path', 
                        help='Output path.')
    return parser

if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    outHTML(args.output,args.path)
