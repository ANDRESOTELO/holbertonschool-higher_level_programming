#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    message = "Unknown format code 'd' for object of type 'str'"
    try:
        int(value)
        print("{:d}".format(value))
        return True
    except ValueError:
        print("Exception: {:s}".format(message), file=sys.stderr)
        return False
    except:
        print("Exception: {:s}".format(message), file=sys.stderr)
        return False
