# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари, реализованные
# по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей
# буквы. Например:
# >>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Сможете ли вы вернуть отсортированный по ключам словарь?
def thesaurus(*args):
    dictionary = {}
    for complete_name in args:
        br_name, last_name = complete_name.split()
        br_letter_of_br_name = br_name[0]
        br_letter_of_last_name = last_name[0]
        dictionary.setdefault(br_letter_of_last_name, {}). \
            setdefault(br_letter_of_br_name, []).append(complete_name)
    return dictionary


i = thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
for br_letter_of_last_name in sorted(i.keys()):
    print(br_letter_of_last_name)
    for br_letter_of_br_name in sorted(i[br_letter_of_last_name].keys()):
        print(f' {br_letter_of_br_name}: {i[br_letter_of_last_name][br_letter_of_br_name]}')
