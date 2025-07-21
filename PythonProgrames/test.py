input = ' python_world'
even = ''
odd = ''

for ch in input[::2]:
    even += ch
for ch in input[1::2]:
    odd += ch
print("even char: ", even, "\odd char: ", odd)

