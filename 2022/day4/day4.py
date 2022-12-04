f = open(r"C:\Code\advent\2022\day4\day4Input.txt")

fully_dupe_sections = 0

for line in f:
    elf1, elf2 = line.split(',')
    elf1_start, elf1_end = elf1.split('-')
    elf2_start, elf2_end = elf2.split('-')

    if int(elf2_start) <= int(elf1_start) and int(elf1_end) <= int(elf2_end) or \
        int(elf1_start) <= int(elf2_start) and int(elf2_end) <= int(elf1_end):
        print(f"{line} contains fully contained")
        fully_dupe_sections += 1

print("fully contained sets: " + str(fully_dupe_sections))