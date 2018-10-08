import time

def getKey(): 
    #Taking the key from system time
    #returns a  10-digit seed value 
    akey = int(time.time())
    #Squaring the key 
    nkey = akey * akey
    #Extracting required number of digits (10) 
    nkey = nkey / 1000000
    nkey = nkey % 1000000000
    #Returning the key value
    return (int(akey),int(nkey))

print("aKey is: ", getKey()[0])
print("Sqr is: ", getKey()[0]**2)
print("nKey is: ----", getKey()[1], "-----") 