marks = [10,20,30,40]
# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 2):
#         print('Adp is the king of his own kingdom')
#     index+=1


for index,mark in enumerate(marks):
    print(mark)
    if(index == 2):
        print('Adp is the king of his own kingdom')
for index,mark in enumerate(marks,start = 1):
    print(mark)
    if(index == 2):
        print('Adp is the king of his own kingdom')

