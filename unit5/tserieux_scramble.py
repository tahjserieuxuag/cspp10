import random
word = "daddyo"
#a function that scrambles one word
def scramble_word(word):
#turn the word into a list
    
    if len(word) >= 4:
        wlist = list(word)  
        
    #scramble everything but the first and last index
        i1 = word[:1]
        il = word[-1:]
        last = wlist[-1]
        wlist = wlist[1:-1]
    
        random.shuffle(wlist)
        wlist.insert(0,i1)
        wlist.insert([-1],il)
        final =''.join(wlist)
        print(final)
        
    
    #put word back together
        
        
    
    #print word
    
#function for scramble sentence
scramble_word(word)