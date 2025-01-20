import pprint
def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        strings_positions = {}
        for index, string in enumerate(strings, start=1):
            current_position = file.tell()
            file.write(string + '\n')
            strings_positions[(index, current_position)] = string
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

pprint.pprint(result)