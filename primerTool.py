#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:29:08 2019

@author: Pablo Carbonell, SYNBIOCHEM
@description: Run the primers generation.
"""
import argparse
import pandas as pd
import csv
import os
import re
import subprocess
import shutil

def rowCol( pos ):
    row = re.search('^(\D+)', pos).group()
    col = int( re.search('(\d+)$', pos).group() )
    return (row,col)

def nextPos( pos ):
    row, col = rowCol( pos )
    if ord(row) < ord('H'):
        npos = chr( ord(row)+1 ) + str(col)
    else:
        npos = 'A' + str(col+1)
    return npos


def configureTool(args):
    template = os.path.join( os.path.dirname(  __file__), 'primers.sh' )
    if not os.path.exists( args.tempFolder ):
       os.makedirs( args.tempFolder )
    script = os.path.join( args.tempFolder, 'job.sh' )
    log = os.path.join( args.tempFolder, 'log.sh' )
    
    if args.plate is not None:
        plate = args.plate 
    else:
        plate =  'None' 
    df = pd.read_csv(args.plasmids)
    icelist = [str(x) for x in df['ICE']]
    # Loop through each plasmid to avoid connection issues
    for ice in icelist:
#    icelist = ' '.join( icelist )
        with open( template ) as hin, open( script, 'w' ) as hout:
            for line in hin:
                line = re.sub( '{{enzymes}}', args.enzymes, line )
                line = re.sub( '{{temp}}', args.temp, line )
                line = re.sub( '{{plates}}', plate, line )
                line = re.sub( '{{plasmids}}', ice, line )
                hout.write( line )
        logout = open(log, 'w')
        print('Primers for plasmid',ice)
        os.chmod(script,777)
        subprocess.call( [script], shell=True, stdout=logout, stderr=logout )
        os.chdir(os.getenv( 'SBC_ASSEMBLY_PATH' ))
        # Output is generated sbc-assembly root folder, it would be better to make a local copy of the code
        outfile1 = 'primer_1_primer_phospho.csv'
        outfile2 = 'primer_1_primer_nonphospho.csv'
        seqs = {}
        primers = pd.read_csv(outfile1)
        for i in primers.index:
            part = primers.loc[i,'Sequence Name']
            partid,sense = part.split('_')
            if partid not in seqs:
                seqs[partid] = {}
            if sense not in seqs[partid]:
                seqs[partid][sense] = primers.loc[i,'Sequence']

        if os.path.exists( outfile1 ):
            os.unlink( outfile1 )
        # Non phosphorylated primers are ignored
        if os.path.exists( outfile2 ):
            os.unlink( outfile2 )
    pos = 'A1'
    table = []
    with open(args.output, 'w') as output:
        for partid in sorted(seqs):
            for sense in sorted(seqs[partid]):
                table.append( (pos, '_'.join([partid,sense]),seqs[partid][sense]) )
            pos = nextPos(pos)
    df1 = pd.DataFrame( table,columns=primers.columns )
    df1.to_csv(args.output, index=False)
                

    return script, log

def arguments():
    parser = argparse.ArgumentParser(description='Read list of primers and output primer plate. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('-iceServer', default=os.getenv('ICE_SERVER'),
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
    parser.add_argument('-tempFolder',
                        help='Tool temporary folder.')
    return parser

if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    script, log = configureTool( args )
    if False:
        logout = open(log, 'w')
        print('Running primers script...')
        os.chmod(script,777)
        subprocess.call( [script], shell=True, stdout=logout, stderr=logout )
        os.chdir(os.getenv( 'SBC_ASSEMBLY_PATH' ))
        # Output is generated sbc-assembly root folder, it would be better to make a local copy of the code
        outfile1 = 'primer_1_primer_phospho.csv'
        outfile2 = 'primer_1_primer_nonphospho.csv'
        if os.path.exists( outfile1 ):
            shutil.copyfile( outfile1, args.output )
            os.unlink( outfile1 )
        # Non phosphorylated primers are ignored
        if os.path.exists( outfile2 ):
            os.unlink( outfile2 )

