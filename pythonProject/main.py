#  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
#  Поскольку разобраться в его кричалках не настолько просто,
#  насколько легко он их придумывает, Вам стоит написать программу.
#  Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
#  в каждой фразе стихотворения одинаковое.
#  Фраза может состоять из одного слова, если во фразе несколько слов,
#  то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
#  Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
#  В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
#  и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

import random as rnd

vowels_lst = ['а', 'е', 'и', 'о', 'у']
consonants_lst = ['п', 'р', 'м']


def syllable(vowels: list, consonants: list) -> str:
    size = rnd.randint(2, 3)
    v = vowels[rnd.randint(0, len(vowels) - 1)]
    return 'п' + v if size == 2 else 'п' + v + consonants[rnd.randint(0, len(consonants) - 1)]


def word(vowels: list, consonants: list) -> str:
    res = [syllable(vowels, consonants) for _ in range(rnd.randint(2, 4))]
    return '-'.join(res)


def sentence(vowels: list, consonants: list) -> str:
    res = [word(vowels, consonants) for _ in range(rnd.randint(1, 5))]
    return ' '.join(res)


print(sent_1 := sentence(vowels_lst, consonants_lst))


def is_rithm(sent: str, vowels: list) -> bool:
    def no_consonants(word: str, vowels: list):
        return ''.join(list(filter(lambda x: x in vowels, word)))

    sent_list = sent.split(' ')
    print(sent_list := list(map(lambda x: no_consonants(x, vowels), sent_list)))
    print(sent_list := list(map(lambda x: len(x), sent_list)))
    print(sent_list2 := list(filter(lambda x: x == max(sent_list), sent_list)))
    return len(sent_list) == len(sent_list2)


print(is_rithm(sent_1, vowels_lst))


# print(lst := list(filter(lambda x: x in vowels_lst, lst)))

