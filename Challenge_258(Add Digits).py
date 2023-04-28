class Solution:

    def add_digits(self, num: int) -> int:
        string_val = str(num)
        print(string_val)
        addition = 0
        for i in string_val:
            addition += int(i)
        if len(str(addition)) != 1:
            return self.add_digits(addition)
        return addition
