# added feature2 branch
print("Feature 2 branch add")
#"""Print duplicat charectes separatly fromthe given word"""

word = "aaaaabbbbbcccddefgh"
dup_ch = ""
for ch in word:
    if word.count(ch) > 1:
        dup_ch += ch
print(dup_ch)