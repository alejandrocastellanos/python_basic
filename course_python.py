mylist = [1,2,3]
for num in range(0,11,2):
    print(num)


list_range = list(range(0,11,2))
print(list_range)


mylist2 = ['a','b','c']
zip_list = zip(mylist, mylist2)
print(zip_list)

# args and kwargs
def num_tuple(*args):
    print(sum(args))
num_tuple(5,4,5)


def dict_kwargs(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(kwargs['fruit'])
    else:
        print('no choise')
dict_kwargs(fruit='apple', veggie='lettuce')

def simple_gen():
    for x in range(3):
        yield x
for number in simple_gen():
    print(number)    
g = simple_gen()
print(next(g))
print(next(g))

from collections import Counter
my_list = [1,1,1,3,3,3,35,666,6,666,6,6]
c = Counter(my_list)
print(c)
print(c.most_common())