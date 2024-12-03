def is_increasing(levels):

    return all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))


def is_decreasing(levels):

    return all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))


def has_valid_differences(levels):

    return all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))


def is_safe_report(levels):

    return (is_increasing(levels) or is_decreasing(levels)) and has_valid_differences(levels)


def analyze_reports(reports):

    safe_count = 0
    for report in reports:
        levels = list(map(int, report.split()))  # Bericht in Zahlen umwandeln
        if is_safe_report(levels):
            safe_count += 1
    return safe_count


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
...
"""


reports = input_data.strip().split("\n")


safe_reports = analyze_reports(reports)
print(safe_reports)

