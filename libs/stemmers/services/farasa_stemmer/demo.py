from farasaStemmer import FarasaStemmer as farasa_stemmer

string = u'مكتبة لمعالجة الكلمات العربية  وتجذيعها'

stems_list = farasa_stemmer.stem(farasa_stemmer, string)

file = open('output.txt', 'w+', encoding="utf-8")

for word in stems_list:
    file.write(word+'\n')

file.close()
