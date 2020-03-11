
import sys

from assembly.app.lcr2 import lcr2, part_pcr, part_qc, part_dig, utils

from assembly import plate, worklist
plates=[]
parts=[]
import os

import writeHtml as WH
from time import gmtime, strftime
from assembly import pipeline
import pandas as pd


def main(args):
    print(args[1])
    ice_helper = utils.ICEHelper(args[2], args[3], args[4])



    plasmid_parts =ice_helper.get_plasmid_parts(args[1:])
 
   # print(len(plasmid_parts))
    


    parts_ice = {ice_id: part_ice
                 for _, parts_map in plasmid_parts.items()
                 for ice_id, part_ice in parts_map.items()
                 if part_ice.get_parameter('Type') != 'DOMINO'}
    part_ids = parts_ice.keys()
    
    start= 0
    parts =[]
    for x in part_ids:
       hold = str(parts_ice.get(x))
       while True:
           try:
               test =hold.index('SBC', start)
           except:
               break
           parts.append(hold[hold.index('SBC', start):hold.index('SBC', start)+9])
           start= hold.index('SBC', start)+9
        
   # for x in parts:
        #print(str(x)+"  parts")
   

    dte = strftime("%y%m%d", gmtime())

    part_vol = 1.0
    pcr_numbers, pcr_df = part_pcr.get_pcr_numbers(plasmid_parts, part_vol)

    outNew =[]
    countNew = []
    for part_id, part_ice in parts_ice.items():
      part_metadata = part_ice.get_metadata()
      for parent in part_metadata['parents']:
       #  print(parent['name'])
         if parent['visible'] == 'OK':
             parent = ice_helper.get_ice_entry(parent['id'])
             linked_parts = parent.get_metadata()['linkedParts']
             if len(linked_parts) < 3:
                 for linked_part in linked_parts:
                     if linked_part['type'] == 'PART':
                         outNew.append(parent.get_ice_id())
                         

    ice_helper.close()
    outNew = list( dict.fromkeys(outNew) ) 
    for x in outNew:
        print(str(x)+"  out")
        countNew.append(0)
    countNew, mapout = get_input_plates('data/plates', outNew, countNew)
    orphan=""
    count=-1
    for x in countNew:
        count =count+1
        if countNew ==0:
           orphan =orphan+str(outNew[count])+" "
          
    WH.writeHtml(mapout, orphan)

def get_input_plates(dir_name, part_ids, countNew):
    '''Get input plates.'''
    input_plates = {}
    mapout=[]
    for(dirpath, _, filenames) in os.walk(dir_name):
        for filename in filenames:
            if filename[-4:] == '.csv':
                df = pd.read_csv(os.path.join(dirpath, filename)) 
                _, name = os.path.split(filename)
                count=-1
                for x in part_ids:
                     count =count+1
                     if x in df.values:
                       mapout.append([name, x])
                       countNew[count] =countNew[count]+1
                    #mel_count= df.str.find(x).sum()
                    #if mel_count>0:
                     #  mapout.append([name, x])
                          #print("yesssitsis")
                       print(name)


 
    return countNew, mapout

if __name__ == '__main__':
    main(sys.argv[0:])


