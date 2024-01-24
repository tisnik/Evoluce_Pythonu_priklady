# Multiprocesing a multithreading v Pythonu:
# - výpočet a vykreslení deseti obrázků Juliových množin
# - každý výpočet je spuštěn v samostatném vláknu
# - explicitní vytvoření vláken, jejich spuštění a čekání na dokončení

from threading import Thread
from time import perf_counter

from palette_mandmap import palette
from PIL import Image

IMAGE_WIDTH = 1024
IMAGE_HEIGHT = 1024


def julia(cx, cy, zx, zy, maxiter):
    """Výpočet počtu iterací pro zadanou konstantu (cx, cy)."""
    c = complex(cx, cy)
    z = complex(zx, zy)
    for i in range(0, maxiter):
        if abs(z) > 2:
            return i
        z = z * z + c
    return 0


def recalc_fractal(filename, xmin, ymin, xmax, ymax, cx, cy, maxiter=1000):
    """Výpočet fraktálu s jeho vykreslením do rastrového obrázku."""
    t1 = perf_counter()
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))

    width, height = image.size
    stepx = (xmax - xmin) / width
    stepy = (ymax - ymin) / height

    y1 = ymin
    for y in range(0, height):
        x1 = xmin
        for x in range(0, width):
            i = julia(cx, cy, x1, y1, maxiter)
            i = 3 * i % 256
            color = (palette[i][0], palette[i][1], palette[i][2])
            image.putpixel((x, y), color)
            x1 += stepx
        y1 += stepy

    # uložení výsledného obrázku
    image.save(filename)

    # výpočet času výpočtu
    t2 = perf_counter()
    print("Done", filename, t2 - t1)


t1 = perf_counter()

# deset vláken s výpočty
t1 = Thread(
    target=recalc_fractal,
    args=(
        "spiral_1.png",
        -1.5,
        -1.5,
        1.5,
        1.5,
        -0.769824999999999998320,
        -0.109270000000000000000,
        1000,
    ),
)
t2 = Thread(
    target=recalc_fractal,
    args=(
        "spiral_2.png",
        -1.5,
        -1.5,
        1.5,
        1.5,
        -0.171119200000000013445,
        0.657309400000000000000,
        1000,
    ),
)
t3 = Thread(
    target=recalc_fractal,
    args=(
        "spiral_3.png",
        -1.5,
        -1.5,
        1.5,
        1.5,
        -0.207190825000000012496,
        0.676656624999999999983,
        1000,
    ),
)
t4 = Thread(
    target=recalc_fractal,
    args=(
        "spiral_4.png",
        -1.5,
        -1.5,
        1.5,
        1.5,
        -0.540623850000000003876,
        0.523798050000000000019,
        1000,
    ),
)
t5 = Thread(
    target=recalc_fractal, args=("julia1.png", -1.5, -1.5, 1.5, 1.5, 0.0, 1.0, 1000)
)
t6 = Thread(
    target=recalc_fractal, args=("julia2.png", -1.5, -1.5, 1.5, 1.5, -1.0, 0.0, 500)
)
t7 = Thread(
    target=recalc_fractal, args=("julia3.png", -1.5, -1.5, 1.5, 1.5, 0.285, 0.01, 1000)
)
t8 = Thread(
    target=recalc_fractal, args=("julia4.png", -1.5, -1.5, 1.5, 1.5, -0.4, 0.6, 1000)
)
t9 = Thread(
    target=recalc_fractal,
    args=("julia5.png", -1.5, -1.5, 1.5, 1.5, -0.835, -0.2321, 1000),
)
t10 = Thread(
    target=recalc_fractal, args=("julia6.png", -1.5, -1.5, 1.5, 1.5, 0.4, 0.4, 1000)
)

# spuštění všech vláken
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

# čekání na dokončení všech vláken
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()

t2 = perf_counter()
print(f"Rendering time: {t2-t1} seconds")
