import random
word = "chenron"
#a function that scrambles one word
def scramble_word(word):
#turn the word into a list
    
    if len(word) >= 4:
        wlist = list(word)  
        
    #scramble everything but the first and last index
        index1 = word[:1]
        lastindex = word[-1:]
        
        wlist = wlist[1:-1]
    
        random.shuffle(wlist)
        wlist.insert(0,index1)
        wlist.append(lastindex)
        final =''.join(wlist)
        print(final)
        
    
    #put word back together
        
        
    
    #print word
    
#function for scramble sentence
scramble_word(word)



