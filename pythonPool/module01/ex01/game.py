class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Tester(GotCharacter):
    """
    Emm just a class to test if got those things right .
    """
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = __class__.__name__
        self.house_words = "Tester is here ?? \'cringe\'"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
