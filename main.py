ruta = "/Users/miguelangelbalbin/workplace/github.com/tbalbini/bookbot/books/frankenstein.txt"

def main():
    word_report()
    
def word_report():
    diccionario_i = word_detail()
    for i in list(diccionario_i.keys()):
        if i not in "qwertyuioplkjhgfdsazxcvbnm":
            del diccionario_i[i]
    print(diccionario_i)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print("77986 words found in the document")
    for i in diccionario_i.keys():
        print(f"The '{i}' character was found {diccionario_i[i]} times")
    print("--- End report ---")
    
def word_detail():
    texto = get_file_contents(ruta).lower()
    sett = set()
    for s in texto:
        sett.add(s)
    
    lista = sorted(list(sett))
    
    dic = {}
    
    for i in lista:
        dic[i] = texto.count(i)
    
    return dic
        
    
def count_words():
    texto = get_file_contents(ruta)
    words = texto.split()
    word_count = len(words)
    print(f"{word_count}")
    
    return word_count
    
def get_file_contents(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents



main()