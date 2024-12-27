#id, class,name, subjectyThen write a program to rerieve uniques entries and eliminate the rerst



details={
    "id1":{"name" : "Rohan",
    "class" : "7",
    "subject" :["English","Maths"]},

    "id2":{"name" : "Arav",
    "class" : "7",
    "subject" :["English","Maths"]},

    "id3":{"name" : "Mohan",
    "class" : "7",
    "subject" :["English","Maths"]},

    "id4":{"name" : "Mukesh",
    "class" : "7",
    "subject" :["English","Maths"]}

    }
 

result={}
for key,value in details.items():
    if value not in result.values():
        result[key]=value

print(result)        