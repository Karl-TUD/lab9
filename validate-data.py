import sys 

def main():
    if len(sys.argv) != 3:
        print("Error: Please supply 2 args. name and number")
        return 

    name, number = sys.argv[1], sys.argv[2]
    if len(name) <= 15 and len(number) <= 10:
        print("PASS")
    else:
        print("FAIL")


if __name__ == "__main__":
    main()
