import pigpio

def main():
    pi = pigpio.pi()
    if not pi.connected:
        print("not connected")
        exit()
    pi.set_mode(2, pigpio.INPUT)
    pi.set_mode(2, pigpio.INPUT)
    pi.set_mode(14, pigpio.INPUT)
    print("Pins set")
    while True:
        pass

if __name__ == "__main__":
    main()
