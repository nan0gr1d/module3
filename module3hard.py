#module3hard
def calculate_structure_sum(struct):
    if isinstance(struct, int) or isinstance(struct, float):
        return struct
    elif isinstance(struct, str):
        return len(struct)
    elif isinstance(struct, dict):
        summa = 0
        for key, value in struct.items():
            summa += calculate_structure_sum(key) + calculate_structure_sum(value)
    else:
        summa = 0
        for item in struct:
            summa += calculate_structure_sum(item)

    return summa

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

#eof-module3hard