"""7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
print("Done")

"""

fname = input('Enter file name: ')
n = 0
total = 0
try:
    fh = open(fname)
    for line in fh:
        if not line.startswith('X-DSPAM-Confidence: '): continue
        n += 1
        confidence = float(line[19:].strip())
        total = total + confidence
        avg_confidence = total/n
    print('Average spam confidence:', avg_confidence)
except:
    print('Not a valid file name.')
    exit()
    

# Same problem, but using a list and statistics import to solve.
"""import statistics

fname = input('Enter file name: ')
n = 0
confidence_list = []
try:
    fh = open(fname)
    for line in fh:
        if not line.startswith('X-DSPAM-Confidence: '): continue
        n += 1
        confidence = float(line[19:].strip())
        confidence_list.append(confidence)
        avg_confidence = statistics.mean(confidence_list)
    print('Average spam confidence: ', avg_confidence)
except:
    print('Not a valid file name.')
    exit()"""


# open a file, read the file, remove all the white spaces to the RIGHT side of each line, print the newly stripped file, but in all uppercase:
"""fh = open('mbox-short.txt')

for line in fh:
    stripped = line.rstrip()
    print(stripped.upper())"""
