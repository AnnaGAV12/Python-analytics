# Напишите функцию для транспонирования матрицы

def transparent_matrix(*a_list: list[[int]]) -> list[()] | str:
    is_transparent = True
    col = len(a_list[0])
    for a in list(a_list):
        if len(a) != col:
            is_transparent = False
    if is_transparent:
        return list(zip(*a_list))
    else:
        return 'Матрицу нельзя транспорировать'


print(transparent_matrix([1, 3, 5], [2, 4, 6]))