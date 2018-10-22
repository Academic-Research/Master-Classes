import serial
import serialDevice
import sys

def main():

    kobuki = serialDevice.Device(   port        = '/dev/ttyUSB0',
                                    baud        = 115200,
                                    bytesize    = serial.EIGHTBITS,
                                    stopbits    = serial.STOPBITS_ONE,
                                    parity      = serial.PARITY_NONE
                                )

    # kobuki.ser.port        = '/dev/ttyUSB0'
    # kobuki.ser.baudrate    = 115200
    # kobuki.ser.bytesize    = serial.EIGHTBITS
    # kobuki.ser.stopbits    = serial.STOPBITS_ONE
    # kobuki.ser.parity      = serial.PARITY_NONE

    print kobuki.connect(timeout = 1)
    
    packet = bytearray()
    # ## Sound
    packet.append(b'\xAA') # Header 0
    packet.append(b'\x55') # Header 1
    packet.append(b'\x05') # Lenght
    packet.append(b'\x03') # Sub-Payload 0 - Header
    packet.append(b'\x03') # Sub-Payload 1 - Lenght
    packet.append(b'\x0F') # Sub-Payload 2 - CMD - Note
    packet.append(b'\xFF') # Sub-Payload 3 - CMD - Note
    packet.append(b'\xFF') # Sub-Payload 4 - CMD - Duration
    checksum = b'\x0A'
    packet.append(checksum) # Checksum
    print len(packet)
    print sys.getsizeof("\xef")

    # seq = packet[2::]

    # for i in seq:
    #     checksum = checksum ^ i
    # print checksum
    
    print kobuki.write(packet)
    # print len(packet)
    # print sys.getsizeof(b'\x00\x00\x00')
    # print len(b'\x00\x00\x00')

    ## Move
    # packet.append(0xAA) # Header 0
    # packet.append(0x55) # Header 1
    # packet.append(0x06) # Lenght
    # packet.append(0x01) # Sub-Payload 0 - Header
    # packet.append(0x04) # Sub-Payload 1 - Lenght
    # packet.append(0xFF) # Sub-Payload 2 - CMD - 
    # packet.append(0xFF) # Sub-Payload 3 - CMD - 
    # packet.append(0xFF) # Sub-Payload 4 - CMD - 
    # packet.append(0xFF) # Sub-Payload 5 - CMD - 
    # packet.append(0x02) # Checksum

    # packet.append(0xAA) # Header 0
    # packet.append(0x55) # Header 1
    # packet.append(0x60) # Lenght
    # packet.append(0x10) # Sub-Payload 0 - Header
    # packet.append(0x40) # Sub-Payload 1 - Lenght
    # packet.append(0xFF) # Sub-Payload 2 - CMD - 
    # packet.append(0xFF) # Sub-Payload 3 - CMD - 
    # packet.append(0xFF) # Sub-Payload 4 - CMD - 
    # packet.append(0xFF) # Sub-Payload 5 - CMD - 
    # packet.append(0x30) # Checksum

    #C0FFFFFFFF208060AA55

    # packet.append(0xC0) # Header 0
    # packet.append(0xFF) # Header 1
    # packet.append(0xFF) # Lenght
    # packet.append(0xFF) # Sub-Payload 0 - Header
    # packet.append(0xFF) # Sub-Payload 1 - Lenght
    # packet.append(0x20) # Sub-Payload 2 - CMD - 
    # packet.append(0x80) # Sub-Payload 3 - CMD - 
    # packet.append(0x60) # Sub-Payload 4 - CMD - 
    # packet.append(0xAA) # Sub-Payload 5 - CMD - 
    # packet.append(0x55) # Checksum


    # for i in packet:
    #     print kobuki.write(i)
     
    
    # print kobuki.write(0x00) # Header 0
    # print kobuki.write(0x03) # Header 1
    # print kobuki.write(0x03) # Lenght
    # print kobuki.write(0x0F) # Payload 0
    # print kobuki.write(0xFF) # Payload 1
    # print kobuki.write(0xFF) # Payload 2
    # print kobuki.write(0xF0) # Checksum

    kobuki.disconnect()

if __name__ == '__main__':
    main()


    # port        = '/dev/ttyUSB0'
    # baudrate    = 115200
    # ser         = serial.Serial(port        = port, 
    #                             baudrate    = baudrate, 
    #                             bytesize    = serial.EIGHTBITS,
    #                             stopbits    = serial.STOPBITS_ONE, 
    #                             parity      = serial.PARITY_NONE
    #                             )
    # if ser.isOpen():
    #     print(ser.name + ' is open...')

    # packet = bytearray()
    # packet.append(0x00) # Header 0
    # packet.append(0x03) # Header 1
    # packet.append(0x03) # Lenght
    # packet.append(0x0F) # Payload 0
    # packet.append(0xFF) # Payload 1
    # packet.append(0xFF) # Payload 2
    # packet.append(0xF0) # Checksum

    # print ser.write(packet)
    # print packet

    # ser.close()