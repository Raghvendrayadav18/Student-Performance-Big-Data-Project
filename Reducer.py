import sys

current_subject = None
current_total = 0

for line in sys.stdin:
    line = line.strip()
    
    subject, marks = line.split("\t")
    marks = int(marks)

    if current_subject == subject:
        current_total += marks
    else:
        if current_subject:
            print(f"{current_subject}\t{current_total}")
        current_subject = subject
        current_total = marks

if current_subject:
    print(f"{current_subject}\t{current_total}")