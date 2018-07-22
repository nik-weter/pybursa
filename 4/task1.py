# -*- utf8 -*-

def letters_count(text):
    text = text.strip()
    s = " .,-:;"
    d = {}

    for i in s:
        text = text.replace(i, "")

    for i in text:
        i = i.lower()
        d[i] = d.get(i, 0) + 1

    t = len(text)

    for i in d:
        d[i] = round(((d.get(i, 0) * 100) / t), 1)

    return d


if __name__ == "__main__":
    test = letters_count("Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.")
    print(test)