# Original creator: virejdasani

import os

count = int(input("How many times do you want to commit? \n"))
auto_push = input("Auto git push when commited? (y/n) \n")

for i in range(count):
	# os.system('git commit --allow-empty -m "New Commit at: $(date)"')
	os.system(f'git commit --allow-empty -m "Commit {i} of {count}"')	

print("Commited " + str(count) + " times")

if auto_push == "y":
	os.system('git push')