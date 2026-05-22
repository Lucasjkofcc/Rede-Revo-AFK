import pyautogui as pg  
import time
import random
import subprocess as sp
import pynput
m = pynput.mouse.Controller()
desligar = input("Deseja desligar? (se sim digite a quantidade de tempo em minutos) \n")
if desligar.strip() != "":
    sp.run(f"shutdown {desligar}",shell=True)
else:
    print("iniciado normalmente")
time.sleep(3)
pg.press(";")
pg.write("kits fome",interval=random.uniform(0.01, 0.2))
time.sleep(random.uniform(0.01, 0.2))
pg.press("enter")
kits = 1
print(f"kits: {kits}")
te = time.time()
te2 = time.time()
afk = random.uniform(60, 600)
peixes_clicados = 0
horas_passadas = 0
horas = time.time()
while True:
    try:
        if time.time() - te >= 60 * 30:
            pg.press(";")
            pg.write("kits fome",interval=random.uniform(0.01, 0.2))
            time.sleep(random.uniform(0.1, 0.2))
            pg.press("enter")
            kits += 1
            print(f"kits: {kits}")
            te = time.time()
        if time.time() - te2 >= afk:
            m.click(pynput.mouse.Button.left)
            afk = random.uniform(60, 600)
            te2 = time.time()
        if pg.locateOnScreen("peixe.png",confidence=0.7,grayscale=True):
            peixes_clicados += 1
            pg.click(pg.locateOnScreen("peixe.png",confidence=0.7,grayscale=True))
            print(f"peixes: {peixes_clicados}")
        if time.time() - horas >= 60 * 60:
            horas_passadas += 1
            horas = time.time()
            print(f"horas passadas: {horas_passadas}")
    except pg.ImageNotFoundException:
        pass
