import re
import pickle

def transliterate(text, mode="ru2en", path2traslitDi='/content/translitDiRu2En.pkl', gost=False):
    """
    Функция для транлитерации с русского на англ. и обратно
    text - str - фраза или слово (ФИО) на русском или транслитерированное на англ.
    path2traslitDi - str - путь до словаря с транслитерациями букв
    gost - bool - флаг True - использование ГОСТ 7.79-2000; False - Приказ МИД № 2113 - Загранпаспорт
    return - text - транслитерированный текст
    """
    # Приказ МИД № 2113 - Загранпаспорт
    # ГОСТ 7.79-2000
    # init translit dictionaries
    di_ru_en = pickle.load(open(path2traslitDi, 'rb'))
    if not gost:
        di_ru_en['Ё'] = 'E'
        di_ru_en['Й'] = 'I'
        di_ru_en['Ц'] = 'TS'
        di_ru_en['Щ'] = 'SHCH'
        di_ru_en['Ъ'] = 'IE'
        di_ru_en['Ь'] = ''
        di_ru_en['Ю'] = 'IU'
        di_ru_en['Я'] = 'IA'
    di_en_ru = {di_ru_en[i]: i for i in di_ru_en}
    if mode == "ru2en":
        return "".join([di_ru_en[i] if i in di_ru_en else i for i in text.upper()])
    if mode == "en2ru":
        # main proces
        text = text.upper()
        output = []
        cnt = 0
        for i in range(len(text)):
            if text[i] in set([' ', '.', ',', '!', '?']):
                output.append(text[i])
                continue
            if cnt:
                cnt = cnt - 1
                continue
            for j in range(4, 0, -1):
                val = text[i: i + j]
                if val in di_en_ru:
                    output.append(di_en_ru[val])
                    cnt = j - 1
                    break
        # after processing
        output = "".join(output)
        output = re.compile(r"Ё").sub("Е", output)
        output = re.compile(r"Й").sub("И", output)
        # output = re.compile(r"ЕЕ").sub("ЕЁ", output)
        output = re.compile(r"ИИ").sub("ИЙ", output)
        return output