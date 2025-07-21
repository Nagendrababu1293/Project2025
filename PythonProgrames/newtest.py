input1 = "aaaabbbccd"   #output = a4b3c2d1
input2 = "d1c2a4b3"     #output = aaaabbbccd

output1 = ''
output2 = ''

for ch in input1:
    if ch not in output1:
        output1 += ch + str(input1.count(ch))

for ch in input2:
    if ch.isalpha():
        x=ch
    else:
        d = int(ch)
        output2 += d*x
        

print(output1,"&&", ''.join(sorted(output2)))