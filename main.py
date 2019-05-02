import pymorphy2
import re
import operator

morph = pymorphy2.MorphAnalyzer()


# функция получения нормальной формы слова, возвращает массив слов
def normal_str(input_str):
    word_list = re.findall(r"[\w']+", input_str)
    res = []
    for word in word_list:
        p = morph.parse(word)[0]
        res.append(p.normal_form)
    return res


# функция для создания словаря с частотой появления каждого слова, возвращает словарь
def createDictWithFrequency(normalWordsArr):
    normalWordsArr = [x for x in normalWordsArr if len(x) > 2]
    res = dict()
    for word in normalWordsArr:
        res[word] = normalWordsArr.count(word)
    return res


# функция выводит результат сортировки в файл
def writeInFile(file, dictionary):
    print("Введите 1, чтобы отсортировать по частоте или 2 по количеству символов:")
    i = int(input())
    if i == 1:
        newDict = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
        for values in newDict:
            file.writelines('%s %s \n' % (values[0], values[1]))
    else:
        keys = sorted(dictionary.keys(), key=len, reverse=True)
        for key in keys:
            file.writelines('%s %s \n' % (key, dictionary[key]))
    return


# название файла
filename = "pymorphy_test"
file_source = open(filename + ".txt")
normalWords = []

file_res = open(filename + "2.txt", "w")

for str in file_source:
    for word in normal_str(str):
        normalWords.append(word)

result = createDictWithFrequency(normalWords)
writeInFile(file_res, result)

print("Файл " + filename + "2.txt сформирован в исходной директории!")
