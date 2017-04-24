def hexdic(base):
    base = str(base)
    return {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "a": "10",
        "b": "11",
        "c": "12",
        "d": "13",
        "e": "14",
        "f": "15",
    }.get(base, base)


class ColourConvert(object):
    def __init__(self, *colour):
        self.colour = colour
        self.coef = 255.0/1515.0

    def toRGB(self):
        hex = self.colour[0]
        hex = list(hex)
        if hex[0] == "#":
            del hex[0]
        hex = "".join(hex)
        r = int((hexdic(hex[0]) + hexdic(hex[1])) * self.coef)
        g = int((hexdic(hex[2]) + hexdic(hex[3])) * self.coef)
        b = int((hexdic(hex[4]) + hexdic(hex[5])) * self.coef)
        return [r, g, b]



print ColourConvert("#ff5566").toRGB()
