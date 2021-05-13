import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    lst = book_to_words()
    largestlen = len(max(lst,key = len)) - 2
    rSorted = countSort(lst,largestlen + 1)
    for i in range(largestlen, -1, -1):
        rSorted = countSort(rSorted, i)
    return rSorted

def countSort(lst, digit):
    count = [0] * 128
    sorted = [None] * len(lst)
    for i in lst:
        if len(i) - 1 < digit:
            k = 0
        else:
            k = ord(i.decode('ascii')[digit])
        count[k] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(lst) - 1, -1, -1):
        if len(lst[i]) - 1 < digit:
            k = 0
        else:
            k = ord(lst[i].decode('ascii')[digit])
        sorted[count[k] - 1] = lst[i]
        count[k] += -1
    return sorted

print(radix_a_book())
