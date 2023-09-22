# Задача 3
# Создайте словарь со списком вещей для похода в 
# качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его 
# максимальную грузоподъёмность. Достаточно вернуть один 
# допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def packing_backpack(items, max_weight):
    backpack = {}
    for item, weight in items.items():
        if weight <= max_weight:
            backpack[item] = weight
            max_weight -= weight
    return backpack

items = {
    "фонарик": 0.2, 
    "палатка": 5.0, 
    "спальный мешок": 2.0, 
    "компас": 0.2, 
    "еда": 1.5, 
    "кружка": 1.0, 
    "вода": 2.0}

max_weight = 8.0

backpack = packing_backpack(items, max_weight)
print(backpack)