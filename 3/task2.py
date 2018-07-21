# -*- utf8 -*-
def get_max_len(s):
    max_len = 0
    max_words = []
    s = s.strip()
    s = s.replace('.', '')
    words = s.split()
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    for word in words:
        if len(word) == max_len:
            max_words.append(word)
    return max_words


if __name__ == "__main__":
    print(get_max_len("Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."))