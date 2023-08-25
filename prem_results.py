results_arr = []
final_arr = []
with open('England Premier League 2018-19 copy.txt', 'r') as raw_data:

    for line in raw_data:
        line = line.split()
        line.remove(':')
        try:
            line.remove('Ham') 
        except:
            pass
        try:
            line.remove('City')
        except:
            pass
        try:
            line.remove('Crystal')
        except:
            pass
        if ('Utd' in line):
            pos = line.index('Utd')
            line[pos-1] = 'ManU'
            line.remove('Utd')
        results_arr.append(line)
    for row in results_arr:
        del row[0]
        del row[0]
        
for line in results_arr:
    if ('Arsenal' in line):
            pos = line.index('Arsenal')
            line[pos] = '"602"'
    if ('ManU' in line):
            pos = line.index('ManU')
            line[pos] = '"680"'
    if ('Leicester' in line):
            pos = line.index('Leicester')
            line[pos] = '"673"'
    if ('Newcastle' in line):
            pos = line.index('Newcastle')
            line[pos] = '"688"'
    if ('Tottenham' in line):
            pos = line.index('Tottenham')
            line[pos] = '"728"'
    if ('Watford' in line):
            pos = line.index('Watford')
            line[pos] = '"600"'
    if ('Brighton' in line):
            pos = line.index('Brighton')
            line[pos] = '"625"'
    if ('Huddersfield' in line):
            pos = line.index('Huddersfield')
            line[pos] = '"664"'
    if ('Chelsea' in line):
            pos = line.index('Chelsea')
            line[pos] = '"630"'
    if ('Fulham' in line):
            pos = line.index('Fulham')
            line[pos] = '"654"'
    if ('Palace' in line):
            pos = line.index('Palace')
            line[pos] = '"642"'
    if ('Bournemouth' in line):
            pos = line.index('Bournemouth')
            line[pos] = '"732"'
    if ('Cardiff' in line):
            pos = line.index('Cardiff')
            line[pos] = '"618"'
    if ('Wolves' in line):
            pos = line.index('Wolves')
            line[pos] = '"740"'
    if ('Everton' in line):
            pos = line.index('Everton')
            line[pos] = '"650"'
    if ('Southampton' in line):
            pos = line.index('Southampton')
            line[pos] = '"713"'
    if ('Burnley' in line):
            pos = line.index('Burnley')
            line[pos] = '"622"'
    if ('Liverpool' in line):
            pos = line.index('Liverpool')
            line[pos] = '"676"'
    if ('West' in line):
            pos = line.index('West')
            line[pos] = '"735"'
    if ('Man' in line):
            pos = line.index('Man')
            line[pos] = '"679"'
            
with open('England Premier League 2018-19 write to.txt', 'r') as raw_data2:
    for line in raw_data2:
        line = line.split()
        index1 = line[2]
        index2 = line[3]
        for row in results_arr:
            if (row[0] == index1 and row[1] == index2):
                try:
                    del line[4]
                    del line[4]
                    line.append(row[2])
                    line.append(row[3])
                except:
                    line.append(row[2])
                    line.append(row[3])
            else:
                pass
            
        final_arr.append(line)  
        
with open('England Premier League 2018-19 write to', 'wt') as results_file:
    for result in final_arr:
        result = ' '.join(result)
        results_file.write(result+'\n')
     
        
        
        
        
        
        #league_table = [["602"], ["680"], ["673"], ["688"], ["728"], 
#               ["600"], ["625"], ["664"], ["630"], ["654"], 
 #               ["642"], ["732"], ["618"], ["740"], ["650"], 
  #              ["713"], ["622"], ["676"], ["735"], ["679"]]

        
                
                
                
                
                
                
                #GP = '0'                
#for result in results_arr:
 #   for team in result:
  #      try:
   #         if len(results_arr[team][:] > 4):
                


                
            
            