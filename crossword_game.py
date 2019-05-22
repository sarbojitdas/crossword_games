import numpy
def word_search(wordlist,crossword):
    # convert the user input into list
    word=list(wordlist)
    word=[ch for ch in wordlist]
    
   
    crossword1=list(reversed(crossword))
  
    row_1=crossword[0][:4]
    row_1.reverse()
    
    row_2=crossword[1][:4]
    row_2.reverse()
  
    row_3=crossword[2][:4]
    row_3.reverse()

    revmatrix=[row_3,row_2,row_1]
    #checking from left to right on row1
    if(word[:1]==crossword[0][:1]) and(word[1:2]==crossword[0][1:2]) and (word[2:3]==crossword[0][2:3]):
        return True
    elif(word[:1]==crossword[0][:1]) and (word[1:2]==crossword[0][1:2]) and (word[2:3]==crossword[0][2:3]) and (word[3:4]==crossword[0][3:4]):
        return True
    elif(word[:1]==crossword[0][1:2]) and (word[1:2]==crossword[0][2:3]) and (word[2:3]==crossword[0][3:4]):
        return True
    #checkinf from left to right on row2
    elif(word[:1]==crossword[1][:1]) and(word[1:2]==crossword[1][1:2]) and (word[2:3]==crossword[1][2:3]):
        return True
    elif(word[:1]==crossword[1][:1]) and (word[1:2]==crossword[1][1:2]) and (word[2:3]==crossword[1][2:3]) and (word[3:4]==crossword[1][3:4]):
        return True
    elif(word[:1]==crossword[1][1:2]) and (word[1:2]==crossword[1][2:3]) and (word[2:3]==crossword[1][3:4]):
        return True
    #checking from left to right on row3
    elif(word[:1]==crossword[2][:1]) and(word[1:2]==crossword[2][1:2]) and (word[2:3]==crossword[2][2:3]):
        return True
    elif(word[:1]==crossword[2][:1]) and (word[1:2]==crossword[2][1:2]) and (word[2:3]==crossword[2][2:3]) and (word[3:4]==crossword[2][3:4]):
        return True
    elif(word[:1]==crossword[2][1:2]) and (word[1:2]==crossword[2][2:3]) and (word[2:3]==crossword[2][3:4]):
        return True
    #checking up to down
    elif(word[:1]==crossword[0][:1]) and word[1:2]==crossword[1][:1] and (word[2:3]==crossword[2][:1]):
        return True
    elif(word[:1]==crossword[0][1:2]) and word[1:2]==crossword[1][1:2] and (word[2:3]==crossword[2][1:2]):
        return True
    elif(word[:1]==crossword[0][2:3]) and word[1:2]==crossword[1][2:3] and (word[2:3]==crossword[2][2:3]):
        return True
    elif(word[:1]==crossword[0][3:4]) and word[1:2]==crossword[1][3:4] and (word[2:3]==crossword[2][3:4]):
        return True
    #checking down to up
    elif(word[:1]==crossword1[0][:1]) and word[1:2]==crossword1[1][:1] and (word[2:3]==crossword1[2][:1]):
        return True
    elif(word[:1]==crossword1[0][1:2]) and word[1:2]==crossword1[1][1:2] and (word[2:3]==crossword1[2][1:2]):
        return True
    elif(word[:1]==crossword1[0][2:3]) and word[1:2]==crossword1[1][2:3] and (word[2:3]==crossword1[2][2:3]):
        return True
    elif(word[:1]==crossword1[0][3:4]) and word[1:2]==crossword1[1][3:4] and (word[2:3]==crossword1[2][3:4]):
        return True
    #checking from right to left row1
    elif(word[:1]==revmatrix[0][:1]) and(word[1:2]==revmatrix[0][1:2]) and (word[2:3]==revmatrix[0][2:3]):
        return True
    elif(word[:1]==revmatrix[0][:1]) and (word[1:2]==revmatrix[0][1:2]) and (word[2:3]==revmatrix[0][2:3]) and (word[3:4]==revmatrix[0][3:4]):
        return True
    elif(word[:1]==revmatrix[0][1:2]) and (word[1:2]==revmatrix[0][2:3]) and (word[2:3]==revmatrix[0][3:4]):
        return True
    #checking from right to left row2
    elif(word[:1]==revmatrix[1][:1]) and(word[1:2]==revmatrix[1][1:2]) and (word[2:3]==revmatrix[1][2:3]):
        return True
    elif(word[:1]==revmatrix[1][:1]) and (word[1:2]==revmatrix[1][1:2]) and (word[2:3]==revmatrix[1][2:3]) and (word[3:4]==revmatrix[1][3:4]):
        return True
    elif(word[:1]==revmatrix[1][1:2]) and (word[1:2]==revmatrix[1][2:3]) and (word[2:3]==revmatrix[1][3:4]):
        return True
    #checking from right to left row3
    elif(word[:1]==revmatrix[2][:1]) and(word[1:2]==revmatrix[2][1:2]) and (word[2:3]==revmatrix[2][2:3]):
        return True
    elif(word[:1]==revmatrix[2][:1]) and (word[1:2]==revmatrix[2][1:2]) and (word[2:3]==revmatrix[2][2:3]) and (word[3:4]==revmatrix[2][3:4]):
        return True
    elif(word[:1]==revmatrix[2][1:2]) and (word[1:2]==revmatrix[2][2:3]) and (word[2:3]==revmatrix[2][3:4]):
        return True

    else:
       return False
    
    
#user input    
    
wordlist = input(str("enter the string="))

crossword = [
   ['p','x','e','n'],
   ['g','d','o','g'],
   ['p','e','n','d']
   ]
print(word_search(wordlist,crossword))   