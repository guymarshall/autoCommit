# Original creator: virejdasani

import os

def commit(i: int, count: int):
	os.system(f"git commit --allow-empty -m \"Commit {i} of {count}\"")

def main():
	count = int(input("How many times do you want to commit? "))
	auto_push = input("Auto git push when commited? (y/n) ")

	for i in range(count):
		commit(i, count)

	print(f"Committed {count} times")

	if auto_push == "y":
		os.system("git push")

if __name__ == "__main__":
	main()
