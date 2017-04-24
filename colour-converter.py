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
        r = float(hexdic(hex[0]) + hexdic(hex[1])) * self.coef
        g = float(hexdic(hex[2]) + hexdic(hex[3])) * self.coef
        b = float(hexdic(hex[4]) + hexdic(hex[5])) * self.coef
        return [int(r), int(g), int(b)]



print ColourConvert("#ab1111").toRGB()
