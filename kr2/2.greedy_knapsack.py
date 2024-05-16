def knapsack_min_weight(capacity, items):
    items.sort(key=lambda x: x[1])  # Сортировка по весу
    knapsack = []
    total_weight = 0
    print("Шаги для минимального веса:")
    for item in items:
        if total_weight + item[1] <= capacity:
            knapsack.append(item)
            total_weight += item[1]
            print(f"Добавлен предмет {item[0]} с весом {item[1]} и стоимостью {item[2]}")
        else:
            print(f"Пропускаем предмет {item[0]} с весом {item[1]} и стоимостью {item[2]} (вес превышает допустимую грузоподъемность)")
    return knapsack


def knapsack_max_value(capacity, items):
    items.sort(key=lambda x: x[2], reverse=True)  # Сортировка по стоимости (убывающая)
    knapsack = []
    total_weight = 0
    print("Шаги для максимальной цены:")
    for item in items:
        if total_weight + item[1] <= capacity:
            knapsack.append(item)
            total_weight += item[1]
            print(f"Добавлен предмет {item[0]} с весом {item[1]} и стоимостью {item[2]}")
        else:
            print(f"Пропускаем предмет {item[0]} с весом {item[1]} и стоимостью {item[2]} (вес превышает допустимую грузоподъемность)")
    return knapsack


def knapsack_max_value_per_weight(capacity, items):
    items.sort(key=lambda x: x[2] / x[1], reverse=True)  # Сортировка по удельной стоимости (убывающая)
    knapsack = []
    total_weight = 0
    print("Шаги для максимальной удельной цены:")
    for item in items:
        if total_weight + item[1] <= capacity:
            knapsack.append(item)
            total_weight += item[1]
            print(f"Добавлен предмет {item[0]} с весом {item[1]} и стоимостью {item[2]}")
        else:
            print(f"Пропускаем предмет {item[0]} с весом {item[1]} и стоимостью {item[2]} (вес превышает допустимую грузоподъемность)")
    return knapsack


capacity = 12
items = [(1, 4, 12), (2, 4, 20), (3, 4, 28), (4, 5, 30), (5, 7, 7), (6, 7, 35)]


print("Минимальный вес:")
print(knapsack_min_weight(capacity, items))
print("\nМаксимальная цена:")
print(knapsack_max_value(capacity, items))
print("\nМаксимальная удельная цена:")
print(knapsack_max_value_per_weight(capacity, items))
