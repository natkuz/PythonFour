# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def dict_from_params(key_one, key_two, key_three, key_four, key_five):
    dict_params = dict(locals()) # так не очень хорошо делать
    dict_keys = {}
    for key, item in dict_params.items():
        if type(item) == list or type(item) == dict or type(item) == set or type(item) == bytearray:
            item = ", ".join(map(str, item))
            dict_keys[item] = key
        dict_keys[item] = key
    return dict_keys


key_one = {1: 1, 2: 2}
key_two = {'two', 'three'}
key_three = [2.2, 1.2]
key_four = bytearray(5)
key_five = 1

print(dict_from_params(key_one, key_two, key_three, key_four, key_five))
