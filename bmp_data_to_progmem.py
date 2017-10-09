#!/usr/bin/env python3

import os, sys, getopt

COLOR_THRESHOLD = 170

def usage():
    print("bmp_data_to_progmem -f <filename> -w <width> -h <height>")


def pretty_print(progmem_array, num_cols):
    count = 0
    for progmem_info in progmem_array:
        count += 1
        print(progmem_info + ", ", end="")
        if count == num_cols:
            print()
            count = 0


def print_as_dots(filename, width, height, inverted):
    with open(filename, "rb") as bmp:
        a_byte = bmp.read(1)
        count = 1

        while a_byte != b"":
            byte_line = int.from_bytes(a_byte, byteorder="big")
            if not inverted:
                if byte_line > COLOR_THRESHOLD:
                    print(".", end="")
                else:
                    print(" ", end="")
                if count % width == 0:
                    print()
            else:
                if byte_line < COLOR_THRESHOLD:
                    print(".", end="")
                else:
                    print(" ", end="")
                if count % width == 0:
                    print()
            count += 1
            a_byte = bmp.read(1)

    total_pixels = count - 1    
    print("Total pixels: ", total_pixels)
    if total_pixels != width * height:
        print("ERROR: Total pixels expected to be " + str(width * height) + ".")


def print_progmem_array(filename, num_cols, inverted):
    all_bytes = []

    with open(filename, "rb") as bmp:
        count = 1
        byte_string = "B"
        a_byte = bmp.read(1)

        while a_byte != b"":
            byte_as_int = int.from_bytes(a_byte, byteorder="big")
            if not inverted:
                if byte_as_int > COLOR_THRESHOLD:
                    byte_as_int = 1
                else:
                    byte_as_int = 0
            else:
                if byte_as_int < COLOR_THRESHOLD:
                    byte_as_int = 1
                else:
                    byte_as_int = 0
            byte_string += str(byte_as_int)

            if count % 8 == 0:
                all_bytes.append(byte_string)
                byte_string = "B"
            count += 1
            a_byte = bmp.read(1)

    pretty_print(all_bytes, num_cols)


def main(args):
    filename = ""
    width = 0
    height = 0
    inverted = False
    num_cols = 0

    print(args)
    try:
        opts, args = getopt.getopt(args, "f:w:h:i", ["filename=", "width=", "height=", "invert"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-f", "--filename"):
            filename = os.path.join(os.getcwd(), arg)
        elif opt in ("-w", "--width"):
            width = int(arg)
            num_cols = width / 8
        elif opt in ("-h", "--height"):
            height = int(arg)
        elif opt in ("-i", "--invert"):
            inverted = True

    if filename == "" or width == 0 or height == 0:
        usage()
        return

    print_as_dots(filename, width, height, inverted)
    print_progmem_array(filename, num_cols, inverted)


if __name__ == "__main__":
    main(sys.argv[1:])
