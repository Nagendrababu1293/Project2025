class EvenOddNumbers:
    input = "PTyetshtoenr"
    def get_even_odd(self):
        self.even_output = self.input[::2]
        print(self.even_output)
        self.odd_output = self.input[1::2]
        print(self.odd_output)

    def get_even_char(self):
        self.even_chr = self.input[::2]
        print(self.even_chr)

    def get_odd_chr(self):
        self.odd_chr = self.input[1::2]
        print(self.odd_chr)





t = EvenOddNumbers()
t.get_even_odd()
t.get_odd_chr()
t.get_even_char()

