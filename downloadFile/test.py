import time
import os

def main():
	while True:
		if os.path.exists(r"E:\contract\contract\2017-04"):
			os.system("taskkill /PID 4996")
			break
		else:
			time.sleep(5)

if __name__ == '__main__':
	main()
