# string = "Figaro, that's a man who loves peanuts. But what about Bond? James Bond?"
# print(string.split(' '))
# time = 0
# result = ''
# for i in string.split(' '):
#     if(time%2 ==1):
#         result += '_'
#     else:
#         result += i
#     time += 1
#
# print(result)
#
# path  = 'G:/chrome//words/words'
# def load_english():
#     """Load and return a collection of english words from a file."""
#     num = 0
#     str_list = []
#     with open(path, 'r') as file:
#         for i in file:
#             str_list.append(i)
#     return str_list
#
# english = load_english()
# print(len(english))
#
#
# def is_triad_word(word, english):
#     """Return whether a word is a triad word."""
#     cell_word1 = word[0::2]
#     cell_word2 = word[1::2]
#     if ('\n' in english[0]):
#         if (cell_word1 + '\n' in english) and ((cell_word2 + '\n' in english)):
#             return True
#     else:
#         if (cell_word1 in english) and ((cell_word2 in english)):
#             return True
#
#     return False
#
# print(is_triad_word('learned', english))
#
#
# def is_triad_phrase(phrase, english):
#     """Return whether a phrase is composed of only triad words."""
#     words = phrase.split(' ')
#     if (is_triad_word(words[0], english)) and (is_triad_word(words[1], english)):
#         return True
#     return  False
#
# print(is_triad_phrase("educated small bird", english))
#
#
# all_triad_words = []
#
# for word in english:
#     #print(word)
#     if is_triad_word(word.replace('\n', ''), english):
#         all_triad_words.append(word)
# print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# print(len(all_triad_words))
#
# def character_gap(ch1, ch2):
#     """Return the absolute gap between two characters."""
#     return abs(ord(ch1) - ord(ch2))
#
# def is_surpassing_word(word):
#     """Return whether a word is surpassing."""
#     num0 = 0
#     num1 = 0
#     for i in range(len(word)-1):
#         num1 = character_gap(word[i], word[i+1])
#         if num1 <= num0:
#             return False
#         num0 = num1
#
#     return True
#
# print(is_surpassing_word('excellent'))
#
# def is_surpassing_phrase(word):
#     """Return whether a word is surpassing."""
#     wrods  = word.split(' ')
#     for i in wrods:
#         if not (is_surpassing_word(i)):
#             return False
#     return  True
#
# print(is_surpassing_phrase("porky hogs"))
# print(int(9/2))
#
# def is_cyclone_word(word):
#     """Return whether a word is a cyclone word."""
#     if len(word) ==1:
#         return True
#     letters = []
#
#     for i in range(int(len(word)/2)):
#         letters.append(word[i])
#         letters.append(word[len(word)-1-i])
#
#     if (len(word)%2)==1:
#         letters.append(word[int(len(word)/2)])
#     tem = letters[:]
#     letters.sort()
#     print(tem)
#     if tem == letters:
#         return True
#     return False
#
# print(is_cyclone_word('a'))
#
# def is_cyclone_phrase(word):
#     """Return whether a phrase is composed only of cyclone words."""
#     words = word.split(' ')
#     for i in words:
#         if not(is_cyclone_word(i)):
#             return False
#     return True
#
# print(is_cyclone_phrase('by myself at twelve pm'))
#
# def is_triangle_word(word):
#     """Return whether a word is a triangle word."""
#     sum = 0
#     for tem in word:
#         print(tem)
#         print(ord(tem)-64)
#         sum += ord(tem)-64
#
#     print(sum)
#     for i in range(sum):
#         if (int(i*(i+1)/2) == sum):
#             return True
#
#     return False
#
# print(is_triangle_word('a'))
#
#
# def self_add(s, n=3):
#     s =s * n
#     return s
#
# def self_mul(s, n=3):
#     for i in range(n):
#         s = s+s
#     return s
#
# print(self_add('s'))
#
# s = 'aaaa\n'
# print(s[:-1])

l = [1,2,3,4,5,6,7,8,9]
l=[]
result = l[2::3]
print(result)
s = '123'
print(s[:-1])