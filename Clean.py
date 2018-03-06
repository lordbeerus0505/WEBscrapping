'''
    Performs cleaning of the Articles present in article.txt
    Following operations have been performed:
    1) Remove Special characters.
    2) Split every line to new line based on full stop and ?
    3) Remove all punctuations and replace(,,:,;, with spaces)
    4) Convert all numbers like 99 , 123 to ninety nine, One hundred and twenty three so on.
    5) Remove all acronyms/abbreviations (write a small piece of code first to find and then remove them )
    6) Replace all occurrence of $, Mr, Mrs, Dr, Prof and so on into their full abbreviated forms .

'''
#from string import maketrans
import re

from num2words import num2words
def int_to_en(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' thousand'
        else: return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' million'
        else: return int_to_en(num // m) + ' million, ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' billion'
        else: return int_to_en(num // b) + ' billion, ' + int_to_en(num % b)

    if (num % t == 0): return int_to_en(num // t) + ' trillion'
    else: return int_to_en(num // t) + ' trillion, ' + int_to_en(num % t)

    raise AssertionError('num is too large: %s' % str(num))


inp=['!@#$%^&*()']
output=['']

fh=open("Articles.txt",'r')#read and write permissions
f=open("Cleaned.txt",'w')
#print(fh.read())
special=[]
dict={'$':'Dollar','Mr':'Mister',"Mrs":"Missus",'Dr':'Doctor','Prof':'Professor'}
for items in fh.read().split():# checks for special symbols
    char =""
    if char in "":
        items=items.translate({ord(c):'' for c in "!@#%^&*()"})#removed all special characters
        items = items.translate({ord(c): ' ' for c in ":;\'\"<>"})  # removed all punctuations
        #replacing words TODO: Use better data structures
        items=items.replace("Dr","Doctor")
        items = items.replace("Mrs", "Missus")
        items = items.replace("Mr", "Mister")
        items = items.replace("Prof", "Professor")


        if  items.isnumeric():
           # print(num2words(items)+"Number printed")
            items=items.replace(items,num2words(items))
            #doesnt work completely
        try:
            val =int(items)
            #now its int
            items=num2words(val)
        except ValueError:
            #ignore
            print(" ")


        if items!='':
            special.append(items)
            print(items+" ",end='')
#if '.' or '?' found add newline
for s in special:
    for ch in s:
        if ch == '.' or ch == '?':
            f.write("\n")

        else:
            f.write(ch)
    f.write(" ")
    print(s)

f.close()


