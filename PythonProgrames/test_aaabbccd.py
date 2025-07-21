from weakref import finalize

input = "abcdabcaba"
output = []
final_output =''


for ch in input:
    if ch not in output:
        output.append(ch)
print(output)
for ch in sorted(output):
    final_output += '{}{}'.format(ch, input.count(ch))
print(final_output  )

new_output = ""
alpha=()
digit =""
for ch in final_output:
    if ch.isalpha():
        x = ch

    else:
        digit = int(ch)
        new_output +=  digit*x
print(new_output)
