t_dict = {'fname':"majid" , 'lname':"gourkani" , 'age':26 , 'job':"pentester"}
m_dict = dict()
print(t_dict.get('age'))
print(t_dict.get('job'))
print(t_dict['fname'])
print(t_dict)
print(type(t_dict))
print(type(m_dict))
print("@@@@@@@@@@@@@@@@@@@@@@@@@")
t_list = ['majid', 'milad', 'saeed', 'vahid']
m_list = list()
print(t_list[2])
t_list.append('hamid')
print(t_list)
print(type(t_list))
print(type(m_list))
print("@@@@@@@@@@@@@@@@@@@@@@@@@")
#tuple is like list, but can't change the elements
t_tuple = ('majid',123,'test',3.14)
m_tuple = tuple(['username','password','address',123])
print(t_tuple[1])
print("@@@@@@@@@@@@@@@@@@@@@@@@@")
