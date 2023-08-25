import csv

filename = 'putts per round.csv'
first = 'Phil Mickleson'
title = filename.strip('.csv')
unit = 'putts per round'

putts_per = []

with open(filename, 'r') as raw_data:
    
    data = csv.reader(raw_data)

    for line in data:
        
        line = ''.join(line)
        
        avg_putts = line.strip(','+'.'+'a'+'b'+'c'+'d'+'e'+'f'+'g'+'h'+'i'+'j'+'k'+'l'+'m'+'n'+'o'+'p'+'q'+'r'+'s'+'t'+'u'+'v'+'w'+'x'+'y'+'z'+'A'+'B'+'C'+'D'+'E'+'F'+'G'+'H'+'I'+'J'+'K'+'L'+'M'+'N'+'O'+'P'+'Q'+'R'+'S'+'T'+'U'+'V'+'W'+'X'+'Y'+'Z'+'''"'''+' '+'í'+'á'+'ó'+"""'"""+'\ufeff'+first)
        
        putts_per.append(float(avg_putts))
        
total_putts_per = sum(putts_per)
avg_putts_per = str(round(total_putts_per/len(putts_per), 2))
        
print('Average PGA Tour '+title+': '+avg_putts_per+' '+unit)