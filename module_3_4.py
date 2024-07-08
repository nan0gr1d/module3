#module_3_4.py
"""
Задача "Однокоренные":
Напишите функцию single_root_words,
которая принимает одно обязательное слово в параметр ,
а далее неограниченную последовательность в параметр *other_words.
Функция должна составить новый список same_words только из тех слов списка other_words,
которые содержат root_word или наоборот root_word содержит одно из этих слов.
После вернуть список same_words в качестве результата своей работы.
"""
def single_root_words(root_word, *other_words):
    some_words = []
    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            some_words.append(word)

    return some_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('foo', 'buz', 'Foo', 'bar', 'oFo', 'FO', 'oO')
print(result1)
print(result2)
print(result3)

#eof-module_3_4