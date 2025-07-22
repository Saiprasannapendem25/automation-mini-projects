bugs = []

print(f"Enter the bugs. Type 'done' when finished")

while True:
    bug = input(f"Enter bug: ")
    if bug.strip().lower() == "done":
        break
    bugs.append(bug)

print("\n....---Bugs Report----")
print(f"Enter total number of bugs: {len(bugs)}")
for i, b in enumerate(bugs, start = 1):
    print(f"Bug {i} : {b}")

