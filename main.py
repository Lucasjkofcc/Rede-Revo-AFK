import pyautogui as pg, subprocess as sp, random, time, os, platform
#Configs
DEBUG = False
KIT_MESSAGE = "kits fome"
KITS_INTERVAL_SEC = 30 * 60
AFK_MIN = 60
AFK_MAX = 600
PEIXE_IMAGE = "peixe.png"
random_digitar = random.uniform(0.01, 0.05) if not DEBUG else 0.02

#Debug Configs
if DEBUG:
    KITS_INTERVAL_SEC = int(input("Intervalo entre kits (segundos): "))
    AFK_MIN = 2
    AFK_MAX = 5
RANDOM_ESPERAR = random.uniform(0.5, 1.5) if not DEBUG else 1.0
def schedule_shutdown(minutes_str):
    if not minutes_str:
        return
    try:
        minutes = int(minutes_str)
    except ValueError:
        print("Valor inválido para desligar:", minutes_str)
        return

    is_windows = platform.system().lower().startswith("win")
    if is_windows:
        seconds = max(0, minutes * 60)
        cmd = f"shutdown -s -f -t {seconds}"
    else:
        if minutes <= 0:
            cmd = "shutdown -h now"
        else:
            cmd = f"shutdown -h +{minutes}"

    print("Executando comando de desligamento:", cmd)
    if DEBUG:
        print("(DEBUG) shutdown simulado — não executando comando")
        return
    try:
        sp.run(cmd, shell=True)
    except Exception as e:
        print("Falha ao executar shutdown:", e)


def send_kits():
    if DEBUG:
        print(f"(DEBUG) send_kits: {KIT_MESSAGE}")
        return
    pg.press(";")
    pg.write(KIT_MESSAGE, interval=random_digitar)
    time.sleep(0.1)
    pg.press("enter")


def main():
    pg.FAILSAFE = True

    desligar = input("Deseja desligar? (se sim digite a quantidade de tempo em minutos) \n").strip()
    if desligar:
        schedule_shutdown(desligar)
    else:
        print("Iniciado normalmente")

    time.sleep(4) #Tempo Alt Tab
    send_kits()
    kits = 1
    print("kits:", kits)

    last_kit = time.time()
    last_afk = time.time()
    afk = random.uniform(AFK_MIN, AFK_MAX)
    peixes = 0
    horas = 0
    last_hour = time.time()

    try:
        while True:
            now = time.time()
            if now - last_kit >= KITS_INTERVAL_SEC:
                send_kits()
                kits += 1
                print("kits:", kits)
                last_kit = now

            if now - last_afk >= afk:
                if DEBUG:
                    print("(DEBUG) AFK click simulated")
                else:
                    pg.click()
                afk = random.uniform(AFK_MIN, AFK_MAX)
                last_afk = now

            if os.path.exists(PEIXE_IMAGE):
                found = pg.locateOnScreen(PEIXE_IMAGE, confidence=0.7, grayscale=True)
                if found:
                    center = pg.center(found)
                    delay = random.uniform(0.5, 3.0)
                    if DEBUG:
                        print("(DEBUG) peixe encontrado em", center, f"— aguardando {delay:.2f}s (simulado)")
                        peixes += 1
                        print("peixes:", peixes)
                    else:
                        time.sleep(delay)
                        pg.click(center)
                        peixes += 1
                        print("peixes:", peixes)

            if now - last_hour >= 60 * 60:
                horas += 1
                last_hour = now
                print("horas passadas:", horas)

    except KeyboardInterrupt:
        print("Finalizado pelo usuário")
    except Exception as e:
        print("Erro inesperado:", e)


if __name__ == "__main__":
    main()
