from sys import stdin

text = []
for line in stdin:
    text.append(line.rstrip('\n').split())

list_word = []
for element in text:
    list_word.extend(element)

result = []
for word in set(list_word):
    if word.lower() == word[::-1].lower():
        result.append(word)
result.sort()
for x in result:
    print(x)
