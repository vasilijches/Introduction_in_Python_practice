# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.

# She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.

# Output: 19

# text = str('She sells sea shells on the sea shore;The shells that she sells are sea shells'
#            ' I\'m sure.So if she sells sea shells on the sea shore,I\'m sure that the shells'
#            ' are seashore shells.  ')
# text = text.replace(',', ' ')
# text = text.replace('.', ' ')
# text = text.replace(';', ' ')
# text = text.replace('-', ' ')
# set_1 = set(text.split(' '))
# set_1.discard('')
# print(set_1)
# print(len(set_1))

# from string import punctuation
#
# text = '''She sells sea shells    on the sea shore;The shells that she sells are sea shells I\'m
#  sure.So if she sells sea shells on the sea shore,I\'m sure that the shells are seashore shells.'''
#
# for ch in punctuation + '-' + '\n':
#     text = text.replace(ch, ' ')
#
# print(len(set(text.lower().split())))

from string import punctuation

text = '''She sells sea shells    on the sea shore;The shells that she sells are sea shells I'm
  sure.So if she sells sea shells on the sea shore,I'm sure that 
  the shells are seashore shells.'''

# rus_letters = ''.join([chr(i) for i in range(ord('а'), ord('я') + 1)]) + 'ё'
# print(rus_letters)

words = []
word = ''
for ch in text.lower():
    if ch.isalpha() or ch == "'":
        word += ch
    else:
        if word != '':
            words.append(word)
        word = ''
print(len(set(words)))
