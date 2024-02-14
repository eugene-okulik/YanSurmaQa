my_tuple = ('apple', 'juice', 1.25, 144, True)
my_list = [1, 2, 3, 'hello', None]
my_dict = {1: 'value1', 'two': 2, 3: 'apple', 4: 'football', 5: 'oneTwoOne'}
my_set = {1, 14, 15, 'go', 'cool', 'red', 1007}

final_dict = {'tuple': my_tuple, 'list': my_list, 'dict': my_dict, 'set': my_set}

print(my_tuple[-1])

my_list.append('last')
my_list.pop(2)  # 'hello'

my_dict['i am a tuple'] = 'random value'
my_dict.pop(5)  # 5: 'oneTwoOne'

my_set.add('new element')
my_set.remove('go')

print(final_dict)
