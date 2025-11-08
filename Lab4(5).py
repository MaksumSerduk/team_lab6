def abcT(text):

    chars = list(text)

    result = set()

    for c in set(chars):
        if chars.count(c) >= 2:
            result.add(c)

    return result

text = input("Введіть текст: ")
copy = abcT(text)
print("Літери, що зустрічаються не менше двох разів:", copy)
