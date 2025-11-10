sentence = input("Введіть речення: ")

sentence = sentence.lower()

for symbol in ".,!?;:-\"'()":
    sentence = sentence.replace(symbol,"")

words = sentence.split()

wCount = {}

for a in words:
    if a in wCount:
        wCount[a] += 1
    else:
        wCount[a] = 1

unique_words = [word for word, count in wCount.items() if count == 1]

print("Слова, що зустрічаються один раз:")
if unique_words:
    for word in unique_words:
        print(word)
else:
    print("Немає таких слів.")
