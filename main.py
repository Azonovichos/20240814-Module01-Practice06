# Module 1 Practice 6
print('Задание 1 - Работа со словарями')
my_dict = {'Opel Astra': 'Х790УТ86', 'Mitsubishi Outlender': 'Т995УН86', 'Toyota Land Cruiser Prado': 'К016УТ116'}
print('Dict:',my_dict)
print('Existing value: ',my_dict['Opel Astra'])
print('Not existing value (method 1): ','Mitsubishi Pajero Sport' in my_dict) # variant 1
print('Not existing value (method 2): ',my_dict.get('Mitsubishi Pajero Sport')) # variant 2
my_dict.update({'KIA Rio': 'А520ЕТ116',
                'Nissan Primera': 'Н905ВУ86'})
print('Adding pairs key-value: ',my_dict)
a=(my_dict.pop('KIA Rio'))
print('Deleting pair: ',my_dict)
print('Deleted pair: ',a)
print('Задание 2 - Работа с множествами')
my_set = {286, 'i386', 'Pentium', 286, (1,2,3,4,5), type, 19.5, 19.5}
print('Множество: ',my_set)
my_set.add('Pentium II')
my_set.add('Xeon')
print('Добавление элементов',my_set)
print(my_set.remove(286))
print('Удаление элемента множества (метод remove): ',my_set)
print(my_set.discard((1,2,3,4,5)))
print('Удаление элемента множества (метод discard): ',my_set)