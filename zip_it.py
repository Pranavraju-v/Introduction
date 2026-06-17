a1={2, 1, 3}
a2={'c', 'a', 'b'}
a3=list(zip(a1, a2))
print(3)
list1=[10, 20 , 30 , 40 , 50]
list2=[100, 200, 300, 400, 500]
for x, y in zip(list1, list2[::-1]):
    print(x, y)

stocks=['Realince', 'Infosys', 'tcs']
price=[1234, 2314, 4321]

new_dict={stocks:prices for stocks,
          prices in zip(stocks, price)}
print(new_dict)