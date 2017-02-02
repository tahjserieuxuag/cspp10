import random
word = "Paris"
#a function that scrambles one word
def scramble_word(word):
#turn the word into a list
    
    if len(word) >= 4:
        wlist = list(word)  
        
    #scramble everything but the first and last index
        wlist = wlist[1:-1]
        random.shuffle(wlist)
        print(wlist)
    
    #put word back together
        
        
    
    #print word
    
#function for scramble sentence
scramble_word(word)