import pigpio
import time

def main():
    pi = pigpio.pi()
    if not pi.connected:
        print("not connected")
        exit()

    pi.set_mode(10, pigpio.OUTPUT)
    pi.set_mode(9, pigpio.INPUT)
    pi.set_mode(4, pigpio.OUTPUT)
    pi.set_mode(24, pigpio.OUTPUT)
    pi.set_mode(11, pigpio.OUTPUT)
    pi.set_mode(8, pigpio.OUTPUT)

    flash_500=[]
    flash_500.append(pigpio.pulse(1<<4, 1<<24, 500000))
    flash_500.append(pigpio.pulse(1<<24, 1<<4, 500000))

    pi.wave_clear()
    pi.wave_add_generic(flash_500)
    f500 = pi.wave_create()

    pi.wave_send_repeat(f500)

    h = pi.spi_open(0,32000,3)
    '''while True:
        pi.spi_write(h,[2, 192, 128])
        (b,d)=pi.spi_read(h,3)
        if b==3:
            print(d)
        else:
            print("No data")'''
    for i in range(15):
        (count, rx_data) = pi.spi_xfer(h, [1,128,29])
        print(count)
        print(rx_data)
        time.sleep(4)
    pi.wave_tx_stop()
    pi.wave_clear()

if __name__ == "__main__":
    main()
