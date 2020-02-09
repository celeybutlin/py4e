"""9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.

The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.

The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.

After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print('File cannot be opened: ', name)

senders = dict()

for line in handle:
    if not line.startswith('From:'): continue
    line = line.strip()
    words = line.split()
    for sender in words:
        if sender == "From:": continue
        if sender in senders:
            senders[sender] += 1
        else:
            senders[sender] = 1

largest = 0
for key in senders:
    if senders[key] > largest:
        largest = senders[key]
        max_sender = key
print(max_sender, largest)  