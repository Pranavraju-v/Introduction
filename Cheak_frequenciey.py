test_dict={'codingal': 2, 'is':2, 'best':2, 'for':2, 'coding':1}
print(test_dict)
K=2
res=0
for key in test_dict:
    if test_dict[key]==K:
        res=res+1
print("The number 2 repeted", res,"times.")