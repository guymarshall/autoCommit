# Original creator: virejdasani

import os

count = int(input("How many times do you want to commit?"))
auto_push = input("Auto git push when commited? (y/n)")

for i in range(count):
	os.system(f'git commit --allow-empty -m "Commit {i} of {count}"')	

print(f"Committed {str(count)} times")

if auto_push == "y":
	os.system('git push')