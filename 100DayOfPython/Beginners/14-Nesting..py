# Dic wiht List
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log)
{'France': ['Paris', 'Lille', 'Dijon'], 'Germany': ['Stuttgart', 'Berlin']}

print(travel_log["France"])
['Paris', 'Lille', 'Dijon']

print(travel_log["France"][1])
Lille

# List with List
nested_list = ["A", "B", ["C", "D"]]
print(nested_list)
['A', 'B', ['C', 'D']]

print(nested_list[2][1])
D
