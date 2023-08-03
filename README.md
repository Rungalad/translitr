# translitr
transliteration from ru2en and from transliterated en2ru with gost7.79-2000 or Order Foreign Ministry № 2113 for foreign passport

## Usage

```python
from translitr import transliterate

# EXAMPLES
# with Order Foreign Ministry № 2113 for foreign passport

toen = transliterate("Яблонева Юлия Сергеевна", gost=False)
toru = transliterate(toen, mode='en2ru', gost=False)
print(toen, "<-->", toru)
# IABLONEVA IULIIA SERGEEVNA <--> ЯБЛОНЕВА ЮЛИЯ СЕРГЕЕВНА

toen = transliterate("Цыпленков Жорж Юрьевич")
toru = transliterate(toen, mode='en2ru')
print(toen, "<-->", toru)
# TSYPLENKOV ZHORZH IUREVICH <--> ЦЫПЛЕНКОВ ЖОРЖ ЮРЕВИЧ

toen = transliterate("Иаков Иосиф Кирианович")
toru = transliterate(toen, mode='en2ru')
print(toen, "<-->", toru)
# IAKOV IOSIF KIRIANOVICH <--> ЯКОВ ИОСИФ КИРЯНОВИЧ

toen = transliterate("Тигреев Искандер Равьялович")
toru = transliterate(toen, mode='en2ru')
print(toen, "<-->", toru)
# TIGREEV ISKANDER RAVIALOVICH <--> ТИГРЕЕВ ИСКАНДЕР РАВЯЛОВИЧ

# with gost7.79-2000

toen = transliterate("Яблонева Юлия Сергеевна", gost=True)
toru = transliterate(toen, mode='en2ru', gost=True)
print(toen, "<-->", toru)
# YABLONEVA YULIYA SERGEEVNA <--> ЯБЛОНЕВА ЮЛИЯ СЕРГЕЕВНА

toen = transliterate("Цыпленков Жорж Юрьевич", gost=True)
toru = transliterate(toen, mode='en2ru', gost=True)
print(toen, "<-->", toru)
# CZYPLENKOV ZHORZH YUR`EVICH <--> ЦЫПЛЕНКОВ ЖОРЖ ЮРЬЕВИЧ

toen = transliterate("Иаков Иосиф Кирианович", gost=True)
toru = transliterate(toen, mode='en2ru', gost=True)
print(toen, "<-->", toru)
# IAKOV IOSIF KIRIANOVICH <--> ИАКОВ ИОСИФ КИРИАНОВИЧ

toen = transliterate("Тигреев Искандер Равьялович", gost=True)
toru = transliterate(toen, mode='en2ru', gost=True)
print(toen, "<-->", toru)
# TIGREEV ISKANDER RAV`YALOVICH <--> ТИГРЕЕВ ИСКАНДЕР РАВЬЯЛОВИЧ
```
