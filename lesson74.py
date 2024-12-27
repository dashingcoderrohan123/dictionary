#Write a program to check the frequency of a value in dictionary 



#{'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

text_dictionary={'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("The original dicititonary is:",text_dictionary)

f=2
res=0
for x in text_dictionary:
    if text_dictionary[x]==f:
        res=res+1

print("The frequency of ",f,"is:",res)


