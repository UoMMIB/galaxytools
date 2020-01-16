#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:29:08 2019

@author: Pablo Carbonell, SYNBIOCHEM
@description: After running design2doe, run doepy and postprocessing 
"""
import argparse
import os
import shutil
import zipfile
import glob
import subprocess
import re

def doepy(input1, input2, input3):
    """ Run doepy, to do: replace by import doepy """
    """ python3 $__tool_directory__/code/sbc-doe/doepy.py $input1 $input2 -j $input3 -v "DoE Template" -o -b -r -V -bro """
    doepypath = os.path.join( os.path.dirname(__file__), 'code', 'sbc-doe', 'doepy.py' )
    call = ['python3', doepypath, input1, input2, '-j', input3, '-v', "DoE Template", '-o', '-b', '-r', '-V', '-bro'] 
    print( ' '.join(call) )
    return subprocess.call( call )

def arguments():
    parser = argparse.ArgumentParser(description='Postprocessing after running design2doe. Pablo Carbonell, SYNBIOCHEM, 2020')
    parser.add_argument('input', help='Input design file')
    parser.add_argument('name', help='Design name')
    parser.add_argument('lib', help='Combinatorial library file')
    parser.add_argument('output', help='Output diagram file')
    parser.add_argument('output2', help='Output zip file')
    return parser

if __name__ == '__main__':
    parser = arguments()
    arg = parser.parse_args()
    for f in glob.glob( os.path.join( os.path.dirname(arg.input),arg.name+'.*') ):
        os.unlink(f)
    doepy( arg.input, arg.name, arg.lib )
    pdf = os.path.join( os.path.dirname(arg.input), arg.name + '.pdf' )
    shutil.copy( pdf, arg.output )
    with zipfile.ZipFile( arg.output2, 'w' ) as myzip:
        for f in glob.glob( os.path.join(os.path.dirname(arg.input),arg.name+'.*') ):
            myzip.write( f,arcname=os.path.basename(f) )
