import json
import csv

# Load tasks from JSON
with open('tasks.json', 'r') as f:
    tasks = json.load(f)

# Display tasks
print("Tasks:")
for t in tasks:
    print(f"{t['id']}. {t['task']} - Done: {t['completed']} (Priority: {t['priority']})")

# Calculate Stats
def show_stats(tasks):
    total = len(tasks)
    done = 0
    total_priority = 0

    for t in tasks:
        if t['completed'] == True:
            done += 1
        total_priority += t['priority']

    pending = total - done
    avg_priority = total_priority / total if total != 0 else 0

    print("\nStats:")
    print("Total tasks:", total)
    print("Completed tasks:", done)
    print("Pending tasks:", pending)
    print("Average priority:", round(avg_priority, 1))

show_stats(tasks)

# Save changes back to file
tasks[0]['completed'] = True
with open('tasks.json', 'w') as f:
    json.dump(tasks, f, indent=4)

# Convert JSON to CSV
with open('tasks.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
    for t in tasks:
        writer.writerow([t['id'], t['task'], t['completed'], t['priority']])



