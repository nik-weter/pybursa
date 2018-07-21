glas = ["A", "E", "I", "O", "U", "Y"]

def count_glas(word):
    count = 0
    for i in word:
        if i.upper() in glas:
            count += 1
    return count

def main(s):
    s = s.strip()
    s = s.split()
    max_count = 0
    for word in s:
        count = count_glas(word)
        if count > max_count:
            max_count = count

    return max_count

if __name__ == "__main__":
    print(main('Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. \
    Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.'))
