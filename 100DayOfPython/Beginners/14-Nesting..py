# Dic with List
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


# Dict with dict
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

