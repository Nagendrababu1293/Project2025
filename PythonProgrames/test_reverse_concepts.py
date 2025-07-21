class Test:

    input = "Automation Testing"
    input_2 = "Automation testing using python and pytest framework"

    def test_rev_str_SlicingOperator(self):
        self.output = self.input[::-1]
        print(self.output)

    def test_rev_str_reversedNjoin_method(self):
        self.rev = reversed(self.input)
        print(self.output)

    def test_rev_str_loop(self):
        self.output = ''
        for ch in self.input[::-1]:
            self.output += ch
        print(self.output)


    """ -----------------------Reverse word order in a string---------------------------------"""

    def test_rev_word_order(self):
        self.input_list = self.input_2.split()
        r=self.input_list[::-1]
        self.output =' '.join(r)
        print(self.output)

    def test_rev_contentOfWord(self):
        self.input_2 =self.input_2.split()
        self.output =[]

        for word in self.input_2:
            self.output.append(word[::-1])
        self.output = ' '.join(self.output)
        print(self.output)






""" Object Creation and calling methods"""
t = Test()
t.test_rev_str_SlicingOperator()
t.test_rev_str_loop()
t.test_rev_str_reversedNjoin_method()

t2 = Test()
t2.test_rev_word_order()
t2.test_rev_contentOfWord()