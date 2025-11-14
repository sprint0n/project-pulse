import matplotlib.pyplot as plt

lines = open("pulse.txt").read().splitlines()
labels = ["Commits", "Files"]
values = [int(lines[0]), int(lines[2])]

file_types = ["py", "yml", "txt", "sh", "png"]
counts = [int(lines[3].split()[0]), int(lines[4].split()[0]), int(lines[5].split()[0]), int(lines[6].split()[0]), int(lines[7].split()[0]),]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

ax1.bar(labels, values, color="#2563eb")
ax1.set_title("Project Activity")

ax2.pie(counts, labels=file_types, autopct="%1.1f%%", colors=["#16a34a","#3b82f6","#facc15"])
ax2.set_title("File Type Breakdown")

plt.tight_layout()
plt.savefig("pulse_dashboard.png")
print("pulse_dashboard.png created")