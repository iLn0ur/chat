"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание,
   соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление
   в формат Unicode и также проверить тип и содержимое переменных.
"""

string_kirs = ['разработка', 'сокет', 'декоратор']

for i in string_kirs:
    print(type(i))
    print(i)

print('\n')
string_unicodes = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442',
                   '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

for i in string_unicodes:
    print(type(i))
    print(i)

print('-'*20)
"""   
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов 
   (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

string_lats = [b'class', b'function', b'method']

for i in string_lats:
    print(type(i))
    print(i)
    print(len(i))

print('-'*20)
""" 
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

string_some = ['attribute', 'класс', 'функция', 'type']

for i in string_some:
    try:
        i = bytes(i, 'ascii')
    except UnicodeEncodeError:
        print('bytes can only contain ASCII literal characters')
    print(type(i))
    print(i)
    print(len(i))

print('-'*20)
""" 
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления 
   в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

string_some = ['разработка', 'администрирование', 'protocol', 'standard']

for i in string_some:
    i = i.encode('utf8')
    print(i)
    i = i.decode('utf8')
    print(i)

print('5', '-'*20)
""" 
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового 
   в строковый тип на кириллице.
"""



import subprocess
import chardet

args = ['ping', '-c 2']
hostnames = ['yandex.ru', 'youtube.com']
for hostname in hostnames:

    args.extend([hostname])
    pings = subprocess.Popen(args, stdout=subprocess.PIPE)
    args.pop()

for line in pings.stdout:
    result = chardet.detect(line)
    #print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

    print('6', '-' * 20)
""" 
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», 
   «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и 
   вывести его содержимое.
"""

with open('test_file.txt', 'r', encoding='utf-8') as tf:
    read_all = tf.read()
    print(read_all)


