
count = 0

def getNumberOfSubset(source, sub, isExit):
    
    if(sub in source):
        global count
        count += 1 
        isExit = True
    else:
        startIndex = source.find(sub[0])
        if(not(isExit) and startIndex >= 0): 
            index = getUnmatchedIndex(source[startIndex:], sub)
            
            count += 1
            getNumberOfSubset(source[index:], sub[index:], isExit)                
    
    
def getUnmatchedIndex(str1, str2):
    index = 1
    while (index < len(str1) and index < len(str2)):
        if(str1[index]==str2[index]):
            index += 1    
        else:
            break        
    return index

#getNumberOfSubset("asdbnm", "adnm", False)
#print(count)