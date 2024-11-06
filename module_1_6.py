#Работа со словарями
myDict = {'plate':'тарелка','to take': 'взять','name': 'имя','face': 'лицо'}
print(myDict['plate'])
myDict['place'] = 'место'
print(myDict['place'])
myDict.update({'table' : 'стол', 'to cook': 'готовить'})
del myDict['plate']

print(myDict)# готово

#Работа с множествами
mySet = {1.09,2,5,2, True ,'хомяк',1,True,'хомяк'}
print(mySet)
mySet.add('garbage')
mySet.add(False)
mySet.discard(5)
print(mySet)