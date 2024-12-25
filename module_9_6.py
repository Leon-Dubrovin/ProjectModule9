def all_variants(text):
    for delta in range(len(text)):
        for left in range(len(text) - delta):
            yield text[left:left + delta + 1]

a = all_variants("abc")
for i in a:
    print(i)