with open("test_log.txt" , "r") as f:
    lines = f.readlines()

pass_count = 0
fail_count = 0

for line in lines:
    if "Passed" in line:
        pass_count += 1
    elif "Failed" in line:
        fail_count += 1

print("Total Passed", pass_count)
print("Total Failed", fail_count)

with open("summary.txt", "w") as f:
    f.write(f"Total Passed: {pass_count}\n")
    f.write(f"Total Failed: {fail_count}\n")