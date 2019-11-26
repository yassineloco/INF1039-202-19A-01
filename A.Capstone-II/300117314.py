@author: Morti
"""

print("welcome to the mashup game")

name1=input("inter one full name(First Last) :")

name2=input("enter another full name(First Last) :")

space=name1 . find (" ")

name1_first=name1[0:space]
name1_last=name1[space+1:len(name1)]

space=name2.find(" ")
name2_first=name2[0:space]
name2_last=name2[space+1:len(name2)]

print(name1_first)
print(name1_last)
print(name2_first)
print(name2_last)

len_name1_first=len(name1_first)
len_name2_first=len(name2_first)
len_name1_last=len(name1_last)
len_name2_last=len(name2_last)
index_name1_first= int(len_name1_first/2)
index_name2_first= int(len_name2_first/2)
index_name1_last= int(len_name1_last/2)
index_name2_last= int(len_name2_last/2)

lefthalf_name1_first= name1_first[0:index_name1_first]
righthalf_name1_first= name1_first[index_name1_first:len_name1_first]

lefthalf_name2_first= name2_first[0:index_name2_first]
righthalf_name2_first= name2_first[index_name2_first:len_name2_first]



lefthalf_name1_last= name1_last[0:index_name1_last]
righthalf_name1_last= name1_last[index_name1_last:len_name1_last]
lefthalf_name2_last= name2_last[0:index_name2_last]
righthalf_name2_last= name2_last[index_name2_last:len_name2_last]


newname1_first=lefthalf_name1_first.capitalize() + \
righthalf_name2_first.lower()
    
newname1_last=lefthalf_name1_last.capitalize() + \
righthalf_name2_last.lower()


newname2_first = lefthalf_name2_first.capitalize() + \
righthalf_name1_first.lower()
newname2_last = lefthalf_name2_last.capitalize() + \
righthalf_name1_last.lower()

print("All done! Here are two possibilities, pick the one you like \
best!")

print(newname1_first, newname1_last)
print(newname2_first, newname2_last)









 
