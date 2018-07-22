# -*- utf8 -*-

text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada."
def limit_text(text, limit=0):
    if len(text) > limit and limit:
        new_limit = limit
        while True:
            if " " in text[new_limit] and text[new_limit] != " ":
                new_limit -= 1
            elif " " not in text[new_limit]:
                new_limit += 1
            else:
                break
    else:
        return text
    return text[:new_limit] + "..."


if __name__ == "__main__":
    print(limit_text(text, 3))