import numpy as np
import matplotlib.pyplot as plt
import time
import os

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_menge(xmin, xmax, ymin, ymax, breite, höhe, max_iter):
    r1 = np.linspace(xmin, xmax, breite)
    r2 = np.linspace(ymin, ymax, höhe)
    n3 = np.empty((breite, höhe))
    for i in range(breite):
        for j in range(höhe):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

def bild_gespeichert_prüfen(flag_datei):
    return os.path.exists(flag_datei)

def bild_gespeichert_setzen(flag_datei):
    with open(flag_datei, 'w') as f:
        f.write('Bild gespeichert')

if __name__ == "__main__":
    start_time = time.time()
    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
    breite, höhe, max_iter = 1000, 1000, 1000
    r1, r2, n3 = mandelbrot_menge(xmin, xmax, ymin, ymax, breite, höhe, max_iter)
    ausführungszeit = time.time() - start_time
    print("Python execution time: {:.2f} Sek".format(ausführungszeit))

    plt.imshow(n3.T, extent=[xmin, xmax, ymin, ymax])
    plt.colorbar()
    plt.title("Mandelbrot-Menge")
    plt.xlabel("Reeller Teil")
    plt.ylabel("Imaginärer Teil")

    dateiname = "fraktal.png"
    plt.savefig(dateiname)
    print(f"Bild als {dateiname} gespeichert")
   

    #plt.show()