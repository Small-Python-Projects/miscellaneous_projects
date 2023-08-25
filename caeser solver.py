import collections
import difflib
import string

common_bigrams = ['th', 'he', 'in', 'er', 'an', 're', 'on', 'at', 'en', 'nd', 'ti', 'es', 'or', 'te', 'of', 'ed', 'is', 'it', 'al', 'ar', 'st', 'nt', 'to']

def main_programme():
    
    message = input('Enter coded message:')
    
    bigram_list = bigrams(message)
    bigram_common_list = common_bigram(bigram_list)
    letter_shift = bigram_cycle(bigram_common_list)
    print('YOUR MESSAGE IS: '+caesar(message, letter_shift))
    
    
def bigrams(message):
    
    text = message
    text_arr = text.split()
    char_arr = []
    bigram_arr = []
    bigram_list = []
    for element in text_arr:
        for char in element:
         
            char_arr.append(char)
            
    counter = 0        
    while counter < (len(char_arr) -1):
        bigram_arr.append([char_arr[counter],char_arr[counter+1]])
        counter = counter +1
        
    for lists in bigram_arr:
        element = ''.join(lists)
        bigram_list.append(element)
        
    return bigram_list
    
    
def common_bigram(bigram_list):
    
    bigram_frequency=collections.Counter(bigram_list)
    bigram_arr = bigram_frequency.most_common(7)
    bigram_common_list = []
   
    
    for element in bigram_arr:
        bigram_common_list.append(element[0])
    
    return bigram_common_list

def bigram_cycle(b_c_l):
    
    bigram_arr = []
    new_bigram_arr = []
    counter = 1
    new_bigram = ''
    letter_shift=0
    new_ratio = 0
    
    while counter < 26:
        for element in b_c_l:
            
            for letter in element:
                if ord(letter)+counter > 122:
                    letter = chr(ord(letter)-26)
                new_letter = chr(ord(letter)-counter)
                
                bigram_arr.append(new_letter)
                new_bigram = ''.join(bigram_arr)
                
            new_bigram_arr.append(new_bigram) 
            bigram_arr=[]
        ratio = difflib.SequenceMatcher(None,new_bigram_arr,common_bigrams).ratio()
        
        if ratio>new_ratio:
            new_ratio = ratio
            letter_shift = counter
        else:
            new_bigram_arr = []
        counter = counter + 1
        
    return letter_shift

def caesar(message, letter_shift):
    string_arr = []
    print(letter_shift)
    for word in message:
        for char in word:
            if (ord(char) in range(97,123)):
                if (ord(char)-letter_shift) < 97:
                    new_char = chr(ord(char)+26-letter_shift)
                   
                if ((ord(char)-letter_shift) > 96):    
                    new_char = chr(ord(char)-letter_shift)
                    
                    
            if (ord(char) in range(65,91)):
                if (ord(char)-letter_shift) < 65:
                    new_char = chr(ord(char)+26-letter_shift)
                    
                else:     
                    new_char = chr(ord(char)-letter_shift)
                    
            if (ord(char) not in range(65,91)) and (ord(char) not in range(97,123)):
                new_char=char
              
            string_arr.append(new_char)
    
    decoded_string = ''.join(string_arr)
    return decoded_string

main_programme()