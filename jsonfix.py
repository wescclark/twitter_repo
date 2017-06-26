import re
import sys
import array
import os.path
import io

#jsonfile = open(sys.argv[1],'r')
#outfile = open(sys.argv[2],'w')

jsonfile = open('C:\\Users\\Zaphikel\\Documents\\Twitter_Fun\\comey.json','r')
outfile = open('C:\\Users\\Zaphikel\\Documents\\Twitter_Fun\\comey.newfix.json','w')
with jsonfile as f:
    outfile.write('[\n')
    outfile.write(f.readline())
    for line in f:
        if len(line)==0:
            print('butts')
            outfile.write(']')
            break
        elif line == '\n':
            continue
        else:
            outfile.write('\n'+','+line)
outfile.write('\n]')
outfile.close()
