f = open(r"C:\Code\advent\2022\day1\adventDay1.txt")
calories = [[]]
i = 0

for line in f:
    if line.isspace():
        i += 1
        calories.append([])
    else:
        calories[i].append(int(line))

cal_totals = []
for elf in calories:
    cal_total = 0
    for cal in elf:
        cal_total += cal
    j = 0
    for total in cal_totals:
        if cal_total > total:
            break
        j += 1
    if j is len(cal_totals):
        cal_totals.append(cal_total)
    else:
        cal_totals.insert(j, cal_total)

top_three_cal_total = sum(cal_totals[:3])
print("Done, answer is: " + str(top_three_cal_total))