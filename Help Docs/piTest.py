import pigpio

def main():
    pi = pigio.pi()
    if not pi.connected:
        print("not connected")
        exit()

    h = pi.spi_open(0,32000,3)

    pi.wpi_wrtie(h,[2, 192, 128])

    (b,d)=pi.spi_read(h,3)

    if b==3:
        print d
    else:
        print("No data")
