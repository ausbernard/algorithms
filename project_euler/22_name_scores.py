from util.file_util import read_file

letter_dictionary = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

names = read_file('name_scores_euler_22.txt')

final_count = 0
total_count = 0
count = 0
for position, name in enumerate(sorted(names), start=1):
    for char in name:
        count += letter_dictionary[char]
        total_count += count
        count = 0
    final_count = final_count + total_count*position 
    total_count = 0

print(final_count)


