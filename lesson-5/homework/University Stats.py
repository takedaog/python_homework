universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(unis):
    students = [u[1] for u in unis]
    tuitions = [u[2] for u in unis]
    return students, tuitions

def mean(data):
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

students, tuitions = enrollment_stats(universities)

print("*" * 30)
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuitions):,}\n")

print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,}\n")

print(f"Tuition mean: $ {mean(tuitions):,.2f}")
print(f"Tuition median: $ {median(tuitions):,}")
print("*" * 30)
