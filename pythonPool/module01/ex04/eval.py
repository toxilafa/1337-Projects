class Evaluator:
    @staticmethod
    def zip_evaluate(list1, list2):
        if isinstance(list1, list) and isinstance(list2, list):
            if len(list1) == len(list2):
                total = 0
                for item1, item2 in zip(list1, list2):
                    if isinstance(item1, (int, float)) and\
                         isinstance(item2, str):
                        total += len(item2) * item1
                    else:
                        return -1
                return total
            else:
                return -1
        else:
            return -1

    @staticmethod
    def enumerate_evaluate(list1, list2):
        if len(list1) == len(list2):
            total = 0
            item1 = enumerate(list1)
            for i, j in item1:
                total += j * len(list2[i])
            return total
        else:
            return -1


# def test_evaluator(coefs, words):
#     """A function to test the Evaluator class"""
#     evl = Evaluator()
#     zip_result = evl.zip_evaluate(coefs, words)
#     enum_result = evl.zip_evaluate(coefs, words)
#     print("Testing with")
#     print(f"words = {words}")
#     print(f"coefs = {coefs}")
#     print(f"zip_evaluate() : {zip_result}")
#     print(f"enumerate_evaluate() : {enum_result}")
#     print()


# if __name__ == '__main__':
#     test_evaluator([1.0, 2.0, 1.0, 4.0, 0.5], ["Le", "Lorem", "Ipsum",
# "est", "simple"])
#     test_evaluator([1, 2, 3], ["a", "b", "c"])
#     test_evaluator([1], ["one", "two"])
#     test_evaluator([1, 2, 3], 42.0)
#     test_evaluator([1, "two", 3], ["a", "b", "c"])
