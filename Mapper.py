import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split(",")

    if len(data) == 3:
        student, subject, marks = data
        print(f"{subject}\t{marks}")