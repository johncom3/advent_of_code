

def is_safe(levels):
    is_increasing = True
    is_decreasing = True
    valid_differences = True

    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]

        if abs(diff) < 1 or abs(diff) > 3:
            valid_differences = False
            break


        if diff <= 0:
            is_increasing = False


        if diff >= 0:
            is_decreasing = False

    return valid_differences and (is_increasing or is_decreasing)


input_data = """
48 51 52 53 52
86 87 88 91 91
22 25 28 31 32 36
65 66 68 69 71 72 75 82
39 42 41 44 47
20 21 22 19 20 22 23 22
25 26 27 29 31 34 33 33
54 57 59 61 58 59 60 64
17 19 20 22 25 26 24 31
86 88 90 91 92 92 93 95
23 25 25 28 26
56 57 59 60 61 61 62 62
73 75 76 76 79 83
10 13 16 16 18 21 23 30
43 45 49 52 55 58 59 61
69 72 76 77 75
....
"""
reports = input_data.strip().split("\n")

safe_count = 0


for report in reports:
    levels = list(map(int, report.split()))


    if is_safe(levels):
        safe_count += 1
        continue


    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safe(modified_levels):
            safe_count += 1
            break

print(safe_count)



