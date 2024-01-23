# Praktická ukázka pattern matchingu:
# - převod barvy z různých reprezentací do barvového prostoru RGB

from dataclasses import dataclass
from enum import Enum


class BasicColor(Enum):
    """Základních osm barev."""
    BLACK = (0, 0, 0)
    RED = (255, 0,0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    WHITE = (255, 255, 255)


@dataclass
class Gray:
    """Reprezentace odstínu šedi celočíselnou hodnotou 0..255."""
    gray : int


@dataclass
class RGB:
    """Reprezentace barvy v barvovém prostoru RGB."""
    red : int
    green : int
    blue : int


@dataclass
class HSV:
    """Reprezentace barvy v barvovém prostoru HSV."""
    hue : float
    saturation: float
    value : float


def scale_rgb(r, g, b):
    """Převod hodnot z rozsahu 0.0-1.0 na celočíselný rozsah 0..255."""
    return RGB(int(255*r), int(255*g), int(255*b))


def hsv_to_rgb(hue, saturation, value):
    """Převod barvy z barvového prostoru HSV do prostoru RGB."""
    if saturation==0:
        return scale_rgb(value, value, value)
    else:
        return hsv_to_rgb_(hue, saturation, value)


def hsv_to_rgb_(hue, saturation, value):
    """Pomocná funkce pro výpočet hodnot RGB."""
    if hue == 1.0:
        hue = 0.0
    i = int(hue*6.0)
    f = hue*6.0 - i

    w = value * (1.0 - saturation)
    q = value * (1.0 - saturation * f)
    t = value * (1.0 - saturation * (1.0 - f))

    match i:
        case 0:
            return scale_rgb(value, t, w)
        case 1:
            return scale_rgb(q, value, w)
        case 2:
            return scale_rgb(w, value, t)
        case 3:
            return scale_rgb(w, q, value)
        case 4:
            return scale_rgb(t, w, value)
        case 5:
            return scale_rgb(value, w, q)


def to_rgb(color):
    """Převod barvy z jakékoli podporované reprezentace do prostoru RGB."""
    match color:
        case Gray(gray):
            return RGB(gray, gray, gray)
        case RGB() as rgb:
            return rgb
        case HSV(hue, saturation, value):
            return hsv_to_rgb(hue, saturation, value)
        case BasicColor() as b:
            return RGB(*b.value)
        case _:
            return f"Invalid color {color}"


# otestování jednotlivých možností

print("Grayscale:")

grayColor1 = Gray(0)
print(to_rgb(grayColor1))

grayColor2 = Gray(255)
print(to_rgb(grayColor2))

print("\nRGB:")

rgbColor1 = RGB(0, 0, 0)
print(to_rgb(rgbColor1))

rgbColor2 = RGB(0, 255, 0)
print(to_rgb(rgbColor2))

rgbColor3 = RGB(255, 255, 255)
print(to_rgb(rgbColor3))

print("\nHSV:")

hsvColor1 = HSV(0.0, 0.0, 1.0)
print(to_rgb(hsvColor1))

hsvColor2 = HSV(0.0, 0.0, 0.5)
print(to_rgb(hsvColor2))

hsvColor3 = HSV(0.0, 1.0, 1.0)
print(to_rgb(hsvColor3))

hsvColor4 = HSV(0.3333, 1.0, 1.0)
print(to_rgb(hsvColor4))

hsvColor5 = HSV(0.6666, 1.0, 1.0)
print(to_rgb(hsvColor5))

hsvColor6 = HSV(1.0, 1.0, 1.0)
print(to_rgb(hsvColor6))

hsvColor7 = HSV(1.0, 0.5, 0.5)
print(to_rgb(hsvColor7))

print("\nBasic colors:")

basicColor1 = BasicColor.BLACK
print(to_rgb(basicColor1))

basicColor2 = BasicColor.RED
print(to_rgb(basicColor2))

basicColor3 = BasicColor.GREEN
print(to_rgb(basicColor3))

basicColor4 = BasicColor.BLUE
print(to_rgb(basicColor4))

basicColor5 = BasicColor.YELLOW
print(to_rgb(basicColor5))

basicColor6 = BasicColor.MAGENTA
print(to_rgb(basicColor6))

basicColor7 = BasicColor.CYAN
print(to_rgb(basicColor7))

basicColor8 = BasicColor.WHITE
print(to_rgb(basicColor8))
