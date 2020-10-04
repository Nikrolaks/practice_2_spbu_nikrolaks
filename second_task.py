# по поводу словаря
# я хотела написать код на с++
# типа (условно) for (int i = 0; obj.ma_smalltable.size() == first_size; i++)
#                   obj.push(i, i);
#                cout << obj.ma_smalltable.size();
# залезть в душу питону и нагадить там
# (других возможных вариантов посмотреть ему в душу как-то не нашлось)
# но установить расширение в вижуалке для работы с ним,
# чтобы он нашел файл заголовков <python.h>,
# оказалось для меня непосильным, так что, прости, без словаря

import re


###
# работа с текстом
###

# ищет среди статистик максимальную
def max_stat_find(stat):
    max_value = 0
    max_name = "stupid"
    for key in stat:
        if max_value < stat[key]:
            max_value = stat[key]
            max_name = key
    return max_name


# считает популярность слов или букв в тексте
def word_and_letter_stat_count(words):
    stat = {}
    while len(words) > 0:
        word = words[0]
        if word in stat:
            stat[word] += 1
        else:
            stat[word] = 1
        words.pop(0)
    return stat


# считает популярность буквы в словах
def letter_in_word_stat_count(text, letter):
    letter_in_text = re.findall(letter, text)
    words = re.findall(r'\w+', text)
    return len(letter_in_text) / len(words)


# собственно, функция, которая возвращает самое популярное слово, букву и среднюю встречаемость
# конкретной буквы в слове
def task_function(text, letter):
    statistics = list()
    words = re.findall(r'\w+', text)
    letters = re.findall(r'\w', text)
    # самое популярное слово
    statistics.append(max_stat_find(word_and_letter_stat_count(words)))
    # самая популярная буква
    statistics.append(max_stat_find(word_and_letter_stat_count(letters)))
    # среднее количество вхождений буквы в слово
    statistics.append(letter_in_word_stat_count(text, letter))
    return statistics


# глаза- и душе-щипательный example
e = task_function('На другой день простившись только с одним графом,'
                  ' не дождавшись выхода дам, князь Андрей поехал домой.'
                  'Уже было начало июня, когда князь Андрей, возвращаясь домой, въехал опять в ту березовую рощу,'
                  ' в которой этот старый, корявый дуб так странно и памятно поразил его. Бубенчики еще глуше '
                  'звенели в лесу, чем полтора месяца тому назад; все было полно, тенисто и густо; и молодые ели,'
                  ' рассыпанные по лесу, не нарушали общей красоты и, подделываясь под общий характер, нежно'
                  ' зеленели пушистыми молодыми побегами.\n'
                  'Целый день был жаркий, где-то собиралась гроза, но только небольшая тучка брызнула на пыль'
                  ' дороги и на сочные листья. Левая сторона леса была темна, в тени; правая мокрая, глянцовитая'
                  ' блестела на солнце, чуть колыхаясь от ветра. Все было в цвету; соловьи трещали и перекатывались'
                  ' то близко, то далеко.\n'
                  '«Да, здесь, в этом лесу был этот дуб, с которым мы были согласны», подумал князь Андрей.'
                  ' «Да где он», подумал опять князь Андрей, глядя на левую сторону дороги и сам того не зная,'
                  ' не узнавая его, любовался тем дубом, которого он искал. Старый дуб, весь преображённый,'
                  ' раскинувшись шатром сочной, темной зелени, млел, чуть колыхаясь в лучах вечернего солнца.'
                  ' Ни корявых пальцев, ни болячек, ни старого недоверия и горя, — ничего не было видно.'
                  ' Сквозь жесткую, столетнюю кору пробились без сучков сочные, молодые листья, так что поверить '
                  'нельзя было, что этот старик произвел их. «Да, это тот самый дуб», подумал князь Андрей, и на '
                  'него вдруг нашло беспричинное, весеннее чувство радости и обновления. Все лучшие минуты его '
                  'жизни вдруг в одно и то же время вспомнились ему. И Аустерлиц с высоким небом, и мертвое '
                  'укоризненное лицо жены, и Пьер на пароме, и девочка, взволнованная красотою ночи, и эта ночь,'
                  ' и луна, — и все это вдруг вспомнилось ему.\n'
                  '«Нет, жизнь не кончена в 31 год, вдруг окончательно, беспеременно решил князь Андрей.'
                  ' Мало того, что я знаю всё то, что есть во мне, надо, чтобы и все знали это: и Пьер, и эта '
                  'девочка, которая хотела улететь в небо, надо, чтобы все знали меня, чтобы не для одного меня'
                  ' шла моя жизнь, чтоб не жили они так независимо от моей жизни, чтоб на всех она отражалась и'
                  ' чтобы все они жили со мною вместе!»\n', 'о')
print(e)

###
# работа с алфавитом
# я знаю, что я здесь не использую ни одной библиотеки
# но как-то не очень понятно, как их вообще можно использовать здесь
###


# создает палиндромы по нечетным шаблонам (прибавляет отображение шаблона наоборот без последней буквы)
def palindromes_by_odd_patterns_create(patterns):
    palindromes = []
    for pattern in patterns:
        size = len(pattern)
        half_size = size - 2
        palindrome = pattern
        if half_size >= 0:
            palindrome += pattern[half_size::-1]
        palindromes.append(palindrome)
    return palindromes


# создает палиндромы по четным шаблонам (прибавляет отображение шаблона наоборот)
def palindromes_by_even_patterns_create(patterns):
    palindromes = []
    for pattern in patterns:
        palindromes.append(pattern + pattern[::-1])
    return palindromes


# создает следующую половинку палиндрома по предыдущей (по длине) половинке
def next_size_palindrome_patterns_create(alphabet, previous_size_palindrome_patterns):
    next_patterns = []
    for pattern in previous_size_palindrome_patterns:
        for letter in alphabet:
            next_patterns.append(pattern + letter)
    return next_patterns


# собственно, функция, которая выдает палиндромы не больше данной длины по данному алфавиту
def palindromes_by_alphabet_create(alphabet, size):
    if size < 1:
        return
    even_half = []
    odd_half = alphabet
    current_odd_half = alphabet
    current_size = 2
    while current_size <= size:
        if current_size % 2:
            odd_half += current_odd_half
        else:
            even_half += current_odd_half
            current_odd_half = next_size_palindrome_patterns_create(alphabet, current_odd_half)

        current_size += 1
    palindromes = palindromes_by_even_patterns_create(even_half) + palindromes_by_odd_patterns_create(odd_half)
    return palindromes


# example
gdd = ['а', 'б', 'в', 'г', 'д', 'е']
print(palindromes_by_alphabet_create(gdd[0:3], 3))
