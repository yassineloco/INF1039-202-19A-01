"""
 capstone project- 2

 """
print('Give me 2 names in the format : FIRST and LAST')
name1 = str(input('\n'))
name2 = str(input('\n'))

name1_list = name1.split(' ')

firstname = str(name1_list[0])
lastname = str(name1_list[-1])

name2_list = name2.split(' ')

firstname_2 = str(name2_list[0])
lastname_2 = str(name2_list[-1])

new_firstname = firstname_2[0:2] + firstname[1:]
new_lastname = lastname_2[0:2] + lastname[-1]

new_name = new_firstname + ' ' + new_lastname
print('the new name in format FIRST and LAST is :{} \n'.format(new_name))
