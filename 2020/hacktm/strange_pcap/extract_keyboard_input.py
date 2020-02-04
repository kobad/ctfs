import sys
from scapy.all import *

keys = {0x04: "a", 0x05: "b", 0x06: "c", 0x07: "d",
        0x08: "e", 0x09: "f", 0x0a: "g", 0x0b: "h",
        0x0c: "i", 0x0d: "j", 0x0e: "k", 0x0f: "l",
        0x10: "m", 0x11: "n", 0x12: "o", 0x13: "p",
        0x14: "q", 0x15: "r", 0x16: "s", 0x17: "t",
        0x18: "u", 0x19: "v", 0x1a: "w", 0x1b: "x",
        0x1c: "y", 0x1d: "z", 0x1e: "1", 0x1f: "2",
        0x20: "3", 0x21: "4", 0x22: "5", 0x23: "6",
        0x24: "7", 0x25: "8", 0x26: "9", 0x27: "0",
        0x28: "<RET>", 0x29: "<ESC>", 0x2a: "<DEL>",
        0x2b: "\t", 0x2c: "<SPACE>", 0x2d: "-", 0x2e: "=",
        0x2f: "[", 0x30: "]", 0x31: "\\", 0x32: "<NON>",
        0x33: ";", 0x34: "'", 0x35: "<GA>", 0x36: ",",
        0x37: ".", 0x38: "/", 0x39: "<CAP>", 0x3a: "<F1>",
        0x3b: "<F2>", 0x3c: "<F3>", 0x3d: "<F4>", 0x3e: "<F5>",
        0x3f: "<F6>", 0x40: "<F7>", 0x41: "<F8>", 0x42: "<F9>",
        0x43: "<F10>", 0x44: "<F11>", 0x45: "<F12>"}

shift_keys = {0x04: "A", 0x05: "B", 0x06: "C", 0x07: "D",
              0x08: "E", 0x09: "F", 0x0a: "G", 0x0b: "H",
              0x0c: "I", 0x0d: "J", 0x0e: "K", 0x0f: "L",
              0x10: "M", 0x11: "N", 0x12: "O", 0x13: "P",
              0x14: "Q", 0x15: "R", 0x16: "S", 0x17: "T",
              0x18: "U", 0x19: "V", 0x1a: "W", 0x1b: "X",
              0x1c: "Y", 0x1d: "Z", 0x1e: "!", 0x1f: "@",
              0x20: "#", 0x21: "$", 0x22: "%", 0x23: "^",
              0x24: "&", 0x25: "*", 0x26: "(", 0x27: ")",
              0x28: "<RET>", 0x29: "<ESC>", 0x2a: "<DEL>",
              0x2b: "\t", "2c": "<SPACE>", "2d": "_", "2e": "+",
              0x2f: "{", 0x30: "}", 0x31: "|", 0x32: "<NON>",
              0x33: "\"", 0x34: ":", 0x35: "<GA>", 0x36: "<",
              0x37: ">", 0x38: "?", 0x39: "<CAP>", 0x3a: "<F1>",
              0x3b: "<F2>", 0x3c: "<F3>", 0x3d: "<F4>", 0x3e: "<F5>",
              0x3f: "<F6>", 0x40: "<F7>", 0x41: "<F8>", 0x42: "<F9>",
              0x43: "<F10>", 0x44: "<F11>", 0x45: "<F12>"}


def main():
    filename = sys.argv[1]
    pcap = rdpcap(filename)

    # get key data
    key_data = []
    for pkt in pcap:
        buf = pkt['Raw'].load
        if buf[22] == 1:
            if len(buf[27:]) == 8:
                key_data.append(buf[27:])

    # analyze key typing
    input_data = ""
    for data in key_data:
        if data[2] == 0 or not(0 in data[3:8]):
            continue
        if hex(data[0]) == '0x2' or hex(data[0]) == '0x20':
            input_data += shift_keys[data[2]]
        else:
            input_data += keys[data[2]]

    print("typing data: {}".format(input_data))


if __name__ == '__main__':
    main()
