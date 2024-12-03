

def parse_input(input_data):

    lines = input_data.strip().split("\n")
    
    list1 = []
    list2 = []

    for line in lines:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)
    
    return list1, list2



def countlist(list1, list2):
    for element in list1:
        count = list2.count(element)
        result.append([element, count])
        
    print("Neue Liste:", result)


def sumresult(result):
    total = 0
    for element in result:
        total += element[0] * element[1] 
    
    return total

input_data = '''

85215   94333
24582   34558
98037   94333
75786   66247
45656   85863
70998   87003
30367   62007
81780   23161
90260   65786
24710   86514
14018   34310
.......

'''

list1, list2 = parse_input(input_data)

result = []

countlist(list1, list2)

print(sumresult(result))
    
    
