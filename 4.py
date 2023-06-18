def is_palindrom_1st_version(string: str):
    return string[:] == string[::-1]

def is_palindrom_2nd_version(string: str):
    is_palindrom = True

    for i in range(len(string)):
        if string[i] != string[0-i-1]:
            is_palindrom = False

    return is_palindrom

string: str = input('Введите строку: ')

print(is_palindrom_1st_version(string))
print(is_palindrom_2nd_version(string))