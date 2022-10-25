
"""
x = 16
y = 34
if x % 2 > 0:
    print(x)
    if y < 4:
        print(y)
else:
    print(x+y)
"""
"""
for cont in range (2,9,3):
    print(cont, end="")

spam = 0
while spam < 5:
    print("Hello")
    spam = spam + 1
    
def greeting(name="world"):
    print("hello", name)
    
greeting ("Juan")
greeting()
"""
height_weight_age = [70, 170,40 ]
grades = [95, 80, 75, 62 ]

def vector_add(v, w):
    return [v_i + w_i
    for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    result = vectors[0] # start with the first vector
    for vector in vectors[1:]: # then loop over the others
        result = vector_add(result, vector) # and add them to the result
        return result
vector_sum(10)