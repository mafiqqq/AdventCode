# Credit goes to https://github.com/AlfonsFiguls for teaching me this "thought process"
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?


import re

def main():

    with open("D:\\Sandbox\AdventCode\Day1\input2.txt") as file:
        lines = [line.strip() for line in file]
        
    print(_map_word(lines))
            

def _map_word(lines):
    
    digitalize = []
    # Convert string to digit value
    CHARS_TO_MAP = {
        "one" : "1",
        "two" : "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    # Method 1:
    for word in lines:
        for key, value in CHARS_TO_MAP.items():
            word = re.sub(key, f"{key}{value}{key}", word)
        digitalize.append(word)
        
    return _find_digits(digitalize)


def _find_digits(digitalize):
    num = []
    for word in digitalize:
        digits = []
        for x in word:
            if x.isdigit():
                digits.append(x)
        num.append(int(digits[0] + digits[-1]))

    return sum(num)

if __name__ == "__main__":
    main()

## Backlog
    
    # Method 2:
    # for word in lines:
    #     print(word)
    #     size = len(word)
    #     i = 0
    #     j = 0
    #     while i <= size:
    #         # print(i)
    #         # print(word[j:i])
    #         if word[j:i].isdigit():
    #             i += 1
    #             j += 1
    #             continue
    #         # if word[j:i] in list(CHARS_TO_MAP.keys()):
    #         if word[j:i] in list(CHARS_TO_MAP.keys()):
    #             word = re.sub(word[j:i], CHARS_TO_MAP[word[j:i]], word)
    #             wordnew = word
    #             i=0
    #             continue
    #         i+=1
    #     print(word)