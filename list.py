my_fruits = ['apple', 'banana', 'lime']
print("Kol elementov v spiske:", len(my_fruits))
print(my_fruits[2])

my_fruits.append('orange')
#print(len(my_fruits))

posts_id = [151, 542, 77, 23]
posts_id.sort()
print("Sort vosrt: ", posts_id)
posts_id.sort(reverse=True)
print("Sort ubivan: ", posts_id)


user_unputs = [True, 'hi', 323]

# список словарей
users = [
    {
        'user_id': 132,
        'user__name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
]

# print(len(users))

my_nums = [10, 50, 0, 5, 100]
my_nums.insert(2, -6)
print(my_nums)

# Задача 1
my_new_list = [46, 78.4, 'sun', True, [2, 3]]
print(my_new_list)
dele = my_new_list.pop(2) # Удалили 3-й элемент
print(my_new_list)
print(len(my_new_list))
my_new_list.reverse() # Поменяли порядок следования 
print(my_new_list)
my_new_list1 = ['day', 'night']
my_new_list += my_new_list1
print(my_new_list)
