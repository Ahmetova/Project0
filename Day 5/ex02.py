import re

with open('input_ex02.txt') as f:
    string = f.readline().strip()
    words = re.findall(r'[a-zA-Z]+', string)
    nums = re.findall(r'\d+', string)
    myfile = open("output_ex02.txt", "w+")
    for i in range(0, len(words)):
        myfile.write(words[i]*int(nums[i]))
