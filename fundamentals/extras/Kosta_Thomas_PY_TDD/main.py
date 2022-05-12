from pickle import TRUE
import unittest

def reverseList(arr):
    arr_len = len(arr)
    for i in range(0, arr_len // 2):
        hldr = arr[i]
        arr[i] = arr[(arr_len - 1) - i]
        arr[(arr_len - 1) - i] = hldr
    return arr

def isPalindrome(str):
    str = str.replace(" ", "").lower()
    arr_len = len(str)
    for i in range(0, arr_len // 2):
        if not str[i] == str[(arr_len - 1) - i]:
            return False
    return True

def coin(coin_total):
    coin_change = []
    coin_q = coin_total // 25
    coin_total = coin_total - (coin_q * 25)
    coin_change.append(coin_q)
    coin_d = coin_total // 10
    coin_total = coin_total - (coin_d * 10)
    coin_change.append(coin_d)
    coin_n = coin_total // 5
    coin_total = coin_total - (coin_n * 5)
    coin_change.append(coin_n)
    coin_change.append(coin_total)
    return coin_change

def factorial(num):
    result = 0
    if num > 1:
        result = num * factorial(num - 1)
        return result
    else:
        return num

def fib(num, isFirst = True):
    result = 0
    if num > 1:
        result = fib(num - 1, False)
        if isFirst: return sum(list(result))
        return (sum(list(result)), result[0])
    else:
        return (1, 0)



# print(reverseList(["a","b","c","d"]))

# print(isPalindrome("racecar"))
# print(isPalindrome("asdf"))

print(coin(87))
print(coin(75))
print(coin(15))
print(coin(44))
print(coin(94))

# print(factorial(5))

# print(fib(8))


class Md_test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(reverseList(["a","b","c","d"]), ["d","c","b","a"])
        self.assertEqual(reverseList([1,2,3,4]), [4,3,2,1])
        self.assertEqual(reverseList(["a",1]), [1,"a"])

    def testTwo(self):
        self.assertEqual(isPalindrome("taco cat"), True)
        self.assertEqual(isPalindrome("racecar"), True)
        self.assertEqual(isPalindrome("Was it a car or a cat I saw"), True)
        self.assertEqual(isPalindrome("Murdrum"), True)
        self.assertEqual(isPalindrome("Madam im Adam"), True)

    def testThree(self):
        self.assertEqual(coin(87),[3,1,0,2])
        self.assertEqual(coin(75),[3,0,0,0])
        self.assertEqual(coin(15),[0,1,1,0])
        self.assertEqual(coin(44),[1,1,1,4])
        self.assertEqual(coin(94),[3,1,1,4])

    def testFour(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(3), 6)

    def testFive(self):
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(8), 21)
        self.assertEqual(fib(4), 3)

    def setUp(self):
        print("running setUp")

    def tearDown(self):
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main()