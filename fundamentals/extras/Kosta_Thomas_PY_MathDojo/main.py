class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self


# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

md2 = MathDojo()

md2.add(1,2).add(4,5,6).add(6,7,8,9)
md2.subtract(1,2).subtract(4,5,6).subtract(6,7,8,9)
print(md2.result) # should print 0