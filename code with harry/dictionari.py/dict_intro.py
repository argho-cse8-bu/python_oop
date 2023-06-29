info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# Acceessing single values
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
# error
#print(info['name2'])
print(info.get('eligible'))

# Acceessing multiple values
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

# acceessing keys
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

# Acceessing key_value pairs
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())