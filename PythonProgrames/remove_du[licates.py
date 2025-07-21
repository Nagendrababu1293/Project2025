text = "programming"
unique_char =""
dup_char = ""
not_repeated_char = ""

for ch in text:
    if ch not in unique_char:
        unique_char += ch
    if text.count(ch) == 1:
        not_repeated_char += ch
    elif ch not in dup_char:
        dup_char += ch
print(unique_char, "\n", dup_char, "\n", not_repeated_char)

words = []