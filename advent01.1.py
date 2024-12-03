
def parse_input(input_data):

    lines = input_data.strip().split("\n")
    
    list1 = []
    list2 = []
    

    for line in lines:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)
    
    return list1, list2


def advent_tool01(list1, list2):
    list1.sort()
    list2.sort()

    
    pairedlist = list(zip(list1, list2))
    
    summeduplist = sum(abs(list1 - list2) for list1, list2 in pairedlist)
    return summeduplist




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
43565   47888
59781   79173
47761   71538
85892   22181
.......

'''

list1, list2 = parse_input(input_data)

print(advent_tool01(list1, list2))




