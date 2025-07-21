from itertools import groupby


class Test:
    input = " A1B6C2D3"
    var = "a4b3c2d1"
    var_2 = "A3Z2B4"
    var_3 = "AAAZZBBBB"
    input_2 = "AAAZZBBBB"

    def test_sort_alpha(self):
        self.alpha = ""
        for ch in self.input:
            if ch.isalpha():
                self.alpha += ch
        print(self.alpha)

    def get_digits(self):
        self.digit = ""
        for ch in self.input:
            if ch.isdigit():
                self.digit += ch
        print(self.digit)

    def test_sorting(self):
        self.alpha =[ch for ch in sorted(self.input) if ch.isalpha()]
        self.digit = [ch for ch in sorted(self.input) if ch.isdigit()]
        self.result = ''.join(self.alpha+self.digit)
        print(self.result)

    def test_1(self):
        self.output = ""
        for ch in self.var:
            if ch.isalpha():
                self.x = ch
            else:
                self.digit = int(ch)
                self.output += self.x  * self.digit
        print(self.output)

    def test_2(self):
        self.output = ''
        for ch in self.var_2:
            if ch.isalpha():
                self.alpha =ch
            else:
                self.digit = int(ch)
                self.output +=self.alpha * self.digit
        print(self.output)

    def test_3(self):
        self.output =''
        self.count =1
        for i in range(1, len(self.input_2)):
            if self.input_2[i] == self.input_2[i -1]:
                self.count +=1
            else:
                self.output += self.input_2[i -1] + str(self.count)
                self.count = 1
        self.output += self.input_2[-1]   + str(self.count)
        print(self.output)

    def test_4(self):
        self.result =""
        self.count =1
        for i in range(1, len(self.var_3)):
            if self.var_3[i] == self.var_3[i  -1]:
                self.count += 1
            else:
                self.result +=  self.var_3[i -1]+str(self.count)
                self.count = 1
        self.result += self.var_3[-1] + str(self.count)
        print(self.result)

    def test_5(self, input_30):
        self.alpha = ''
        self.digit =""
        for ch in input_30:
            if ch.isalpha():
                self.alpha += ch
            if ch.isdigit():
                self.digit += ch
        self.output = ''.join(sorted(self.alpha)+sorted(self.digit))
        print(self.output)













t = Test()
# t.test_sort_alpha()
# t.get_digits()
# t.test_sorting()
# t.test_1()
# t.test_2()
# t.test_4()
# t.test_3()
t.test_5("a2d4b1c3")

