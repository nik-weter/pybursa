# -*- utf8 -*-

def revers_word(word):
    return word[::-1]

def revers_phrase(phrase):
    phrase = phrase.strip()
    phrase = phrase.replace(".", "")
    phrase = phrase.split()
    phrase.reverse()
    for j in range(len(phrase)):
        phrase[j] = revers_word(phrase[j])
    res = " ".join(phrase)
    return res

def reverse_string(s):
    s = s.split(". ")
    s.reverse()
    for i in range(len(s)):
        s[i] = revers_phrase(s[i])
    res_str = ". ".join(s)
    return res_str+"."

# def main(s):
#     s = reverse_string(s)
#     lst = s.split(". ")
#     for i in

if __name__ == "__main__":
    result = reverse_string("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. Cras ultricies ligula sed magna dictum porta.")
    print(result)