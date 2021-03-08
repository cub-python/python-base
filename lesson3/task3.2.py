
#  2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
# >>>>>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
# >>> num_translate_adv("tWo")

dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'}


def translate_num(wd):
    tp_wd = wd[0].lower() + wd[1:]  # tp_wd временные получ слова(переменная),первая буква вр слов может быть с больш или с мал буквой. Независимо
    ru_wd = dictionary.get(tp_wd)
    if ru_wd is not None:
        if tp_wd[0] == wd[0]:
            return ru_wd
        else:
            return ru_wd[0].upper() + ru_wd[1:]


print(translate_num('oNe'))
print(translate_num('two'))
print(translate_num('Two'))
print(translate_num('sIx'))
