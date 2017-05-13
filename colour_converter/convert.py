import sys
import math

def hexdic(base):
    base = str(base)
    return {
        "0": "00",
        "1": "01",
        "2": "02",
        "3": "03",
        "4": "04",
        "5": "05",
        "6": "06",
        "7": "07",
        "8": "08",
        "9": "09",
        "a": "10",
        "b": "11",
        "c": "12",
        "d": "13",
        "e": "14",
        "f": "15",
    }.get(base, base)

def RGBdic(base):
    base = str(base)
    return {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }.get(base, base)


class ColourConvert(object):
    def __init__(self, *colour):
        self.colour = colour

    def toRGB(self):
        hex = self.colour[0]
        hex = list(hex)
        if hex[0] == "#":
            del hex[0]
        hex = "".join(hex)
        r = ( float(hexdic(hex[0])) * 16) + (float(hexdic(hex[1])) )
        g = ( float(hexdic(hex[2])) * 16) + (float(hexdic(hex[3])) )
        b = ( float(hexdic(hex[4])) * 16) + (float(hexdic(hex[5])) )
        return [int(r), int(g), int(b)]

    def toHex(self):
        r = int(self.colour[0])
        g = int(self.colour[1])
        b = int(self.colour[2])

        if r > 255:
            return "Numbers cannot be above 255"
        if g > 255:
            return "Numbers cannot be above 255"
        if b > 255:
            return "Numbers cannot be above 255"

        r1 = (int(math.floor(r / 16)))
        r2 = r - (r1 * 16)
        g1 = (int(math.floor(g / 16)))
        g2 = g - (g1 * 16)
        b1 = (int(math.floor(b / 16)))
        b2 = b - (b1 * 16)

        r = "#" + RGBdic(r1) + RGBdic(r2)
        g =       RGBdic(g1) + RGBdic(g2)
        b =       RGBdic(b1) + RGBdic(b2)

        hexa = "".join([r, g, b])

        return hexa

def main():
    if len(sys.argv) == 4:
        print(ColourConvert(sys.argv[1], sys.argv[2], sys.argv[3]).toHex())
    elif len(sys.argv) == 2:
        print(ColourConvert(sys.argv[1]).toRGB())
    else:
        print("Please enter your colour in a valid format, e.g. RGB: '250 30 59' or HEX: \"#a493f4\" or a493f4 EXACTLY\n")
