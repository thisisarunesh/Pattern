import sys
from string import ascii_uppercase, ascii_lowercase, digits

maximum_length = 20276

def generate_pattern(length):
    if length <= maximum_length:
        pattern = ""
        for uppercase in ascii_uppercase:
            for lowercase in ascii_lowercase:
                for digit in digits:
                    if len(pattern) <= length:
                        pattern += uppercase + lowercase + digit
                    else:
                        return pattern[:length]
    else:
        print("ERROR: Generate a pattern of the given length, up to a maximum of 20276")
        sys.exit(0)

def find_position(address):
    try:
        striped_address = address[2:]
        decoded_address = bytearray.fromhex(striped_address).decode("ascii")
        reversed_address = decoded_address[::-1]
        pattern = ""
        for uppercase in ascii_uppercase:
            for lowercase in ascii_lowercase:
                for digit in digits:
                    pattern += uppercase + lowercase + digit
        if pattern.find(reversed_address) > -1:
            return pattern.find(reversed_address)
        else:
            print("Could not find {0} anywhere in the pattern".format(sys.argv[1]))
            sys.exit(0)
    except Exception as error:
        print("Error: Failed to search")
        sys.exit(0)

def help():
    print("Usage: {0} <length> or <pattern>".format(sys.argv[0]))
    print("Generate a pattern of LENGTH or search for PATTERN and return its position in pattern")

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].isdigit():
            result = str(generate_pattern(int(sys.argv[1])))
            print("Generated pattern: {0}".format(result))
            sys.exit(0)
        elif sys.argv[1].startswith("0x"):
            result = int(find_position(str(sys.argv[1])))
            print("The given pattern {0} starts at position: {1}".format(sys.argv[1], result + 1))
            sys.exit(0)
        elif sys.argv[1] == "--help":
            help()
            sys.exit(0)
        else:
            print("Try --help")
    else:
        print("Try --help")

if __name__ == "__main__":
    main()
