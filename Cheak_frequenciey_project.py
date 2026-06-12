dict={'Codingal':3, 'is':2, 'best':2, 'for':2, 'coding':1}
print(dict)
y=int(input("ENter value you want to cheak the frequenciy: "))
res=0
for key in dict:
    if dict[key]==y:
        res=res+1
print(res)