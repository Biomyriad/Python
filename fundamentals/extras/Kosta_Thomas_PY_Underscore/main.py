class Underscore:
    def map(self, iterable, callback):
        ret_arr = []
        for item in iterable:
            ret_arr.append(callback(item))
        print(ret_arr)
        return ret_arr
    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                print(item)
                return item
        return None
    def filter(self, iterable, callback):
        ret_arr = []
        for item in iterable:
            if callback(item):
                ret_arr.append(item)
        print(ret_arr)
        return ret_arr
    def reject(self, iterable, callback):
        ret_arr = []
        for item in iterable:
            if not callback(item):
                ret_arr.append(item)
        print(ret_arr)
        return ret_arr

_ = Underscore() 
_.map([1,2,3], lambda x: x*2) # should return [2,4,6]
_.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
_.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]