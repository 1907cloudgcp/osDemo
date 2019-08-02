import os

def main():
	os.fork()
	print(os.getpid())

if __name__ == '__main__':
	main()
