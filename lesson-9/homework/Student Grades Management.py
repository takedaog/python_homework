import csv

grades = []

with open('grades.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        grades.append(row)

subject_totals = {}
subject_counts = {}

for row in grades:
    subject = row['Subject']
    grade = int(row['Grade'])
    if subject not in subject_totals:
        subject_totals[subject] = grade
        subject_counts[subject] = 1
    else:
        subject_totals[subject] += grade
        subject_counts[subject] += 1

averages = {}
for subject in subject_totals:
    averages[subject] = round(subject_totals[subject] / subject_counts[subject], 1)

with open('average_grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Subject', 'Average Grade'])
    for subject, avg in averages.items():
        writer.writerow([subject, avg])
