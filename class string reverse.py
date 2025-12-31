class String:
    def __init__(self, string):
        self.string = string


class Reverse(String):
    def reverse(self):
        return self.string[::-1]


sentence = Reverse("Today is the last day of the year")
print(sentence.reverse())
