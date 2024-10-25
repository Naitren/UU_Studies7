my_dict = {'Olya':2000, 'Alex':1999, 'Masha':2001}
print(my_dict)
print(my_dict['Olya'], my_dict.get('Larisa'))
my_dict.update({'Marina':1998, 'Katya':2000})
print(my_dict)
a = my_dict.pop('Alex')
print(a)
print(my_dict)

my_set = {1, 2.5, True, 'string', 1, 'string'}
print(my_set)
my_set.update({2, 'apple'})
print(my_set)
print(my_set.discard(2.5))
print(my_set)