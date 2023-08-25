import csv

dist_dict = {}
acc_dict = {}

with open('driving_distance.csv', 'r') as dist_file:
    
    dist_data = csv.reader(dist_file)

    for line in dist_data:
        
        line = ''.join(line)
        
        name = line.strip(','+'.'+'0'+'1'+'2'+'3'+'4'+'5'+'6'+'7'+'8'+'9'+'''"'''+'\ufeff')
        dist = line.strip(','+'.'+'a'+'b'+'c'+'d'+'e'+'f'+'g'+'h'+'i'+'j'+'k'+'l'+'m'+'n'+'o'+'p'+'q'+'r'+'s'+'t'+'u'+'v'+'w'+'x'+'y'+'z'+'A'+'B'+'C'+'D'+'E'+'F'+'G'+'H'+'I'+'J'+'K'+'L'+'M'+'N'+'O'+'P'+'Q'+'R'+'S'+'T'+'U'+'V'+'W'+'X'+'Y'+'Z'+'''"'''+' '+'í'+'á'+'ó'+"""'"""+'\ufeffRory Mcilroy')
         
        dist_dict[name] = [float(dist)]

with open('driving_accuracy.csv', 'r') as acc_file:
    
    acc_data = csv.reader(acc_file)

    for line in acc_data:
        
        line = ''.join(line)
        
        name = line.strip(','+'.'+'0'+'1'+'2'+'3'+'4'+'5'+'6'+'7'+'8'+'9'+'''"'''+'\ufeff')
        acc = line.strip(','+'.'+'a'+'b'+'c'+'d'+'e'+'f'+'g'+'h'+'i'+'j'+'k'+'l'+'m'+'n'+'o'+'p'+'q'+'r'+'s'+'t'+'u'+'v'+'w'+'x'+'y'+'z'+'A'+'B'+'C'+'D'+'E'+'F'+'G'+'H'+'I'+'J'+'K'+'L'+'M'+'N'+'O'+'P'+'Q'+'R'+'S'+'T'+'U'+'V'+'W'+'X'+'Y'+'Z'+'''"'''+' '+'í'+'á'+'ó'+"""'"""+'\ufeffHenrik Stenson')
         
        acc_dict[name] = float(acc)

for key, value in dist_dict.items():
    dist_dict[key].append(acc_dict[key])
    
comb_dict = dist_dict

for key,value in comb_dict.items():
    new_value = round((value[0]**(1.75))*(value[1]**0.5), 2)
    comb_dict[key] = dist_dict[key].append(new_value)
    myorder=[2,0,1]
    value = [ value[i] for i in myorder]
    comb_dict[key] = value
    
sort_comb_dict = sorted(comb_dict.items(), key=lambda kv: kv[1])

file = open('best_drivers.txt', 'w')

for position,player in enumerate(list(reversed(sort_comb_dict))):
    position = str(position+1)
    player_str = str(player[0])
    stats = player[1]
    score = str(stats[0])
    drive = str(stats[1])
    accuracy = str(stats[2])
    file.write('\n\n'+position+'. '+player_str+':-\n Score: '+score+'  Avg. dist.: '+drive+' Yards  fairways hit: '+accuracy+'%')
    
file.close()