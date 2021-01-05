#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        int(value)
        print("{:d}".format(value))
        return True
    except ValueError:
        print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)
        return False
    except:
        print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)
        return False
