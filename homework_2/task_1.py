# Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def convert_number(num: int, mode: str) -> str:
    result = ''
    convert: int = 2
    match mode:
        case "bin":
            convert = 2
        case "oct":
            convert = 8
        case "hex":
            convert = 16
    while num >= 1:
        res = num % convert
        result += str(res)
        num = num // convert
    return result[::-1]

print(convert_number(21, mode="bin"), f"assert: {bin(21)}")
print(convert_number(21, mode="oct"), f"assert: {oct(21)}")
print(convert_number(21, mode="hex"), f"assert: {hex(21)}")