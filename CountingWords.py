introString=input("write your input")
charcterCount=0
wordCount=1
for i in introString:
    charcterCount=charcterCount+1
    if(i==" "):
        wordCount=wordCount+1

print("number of charcters")
print(charcterCount)
print("number of words")
print(wordCount)