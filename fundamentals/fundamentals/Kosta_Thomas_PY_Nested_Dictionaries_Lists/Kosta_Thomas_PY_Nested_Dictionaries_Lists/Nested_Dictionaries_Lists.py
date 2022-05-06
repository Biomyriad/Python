# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
print (students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"])

# Change the value 20 in z to 30
z[0]["y"] = 30
print(z)

##############################################################################

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# 2. Iterate Through a List of Dictionaries

def iterateDictionary(arr):
    for i in range(len(arr)):
        output = ""
        for k,v in arr[i].items():
            if output == "": 
                output += f"{k} - {v}, "
            else:
                output += f"{k} - {v}"
        print(output)   # I think the assignment wanted the use of print(str, end="")
                        #   but that leaves a trailing comma and space if extra logic was not included

def exampleIterateDictionary(arr):
    for i in range(len(arr)):
        isFirstLoop = True
        for k,v in arr[i].items():
            if isFirstLoop: 
                print(f"{k} - {v}, ", end="")
                isFirstLoop = False
            else:
                print(f"{k} - {v}")                      

iterateDictionary(students) 
exampleIterateDictionary(students) 

# 3. Get Values From a List of Dictionaries

def iterateDictionary2(key, arr):
    for i in range(len(arr)):
        print(arr[i][key])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

##############################################################################

# 4. Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictLists):
    for k,v in dictLists.items():
        print("---------------")
        print(f"{len(v)} {k.upper()}")
        for i in v:
            print(i)

printInfo(dojo)