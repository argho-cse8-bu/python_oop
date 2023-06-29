import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
x = int(timestamp)
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
if x<12:
    print('Good morning sir')
elif x>=12 and x<4:
    print('Good afternoon sir')
else:
    print('Good night sir')