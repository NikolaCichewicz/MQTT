import sys
version = "0.6"
PRINT_NON_IMPORTANT = True

# Hex to integer
def hti(b, bo=sys.byteorder):
    return int.from_bytes(b, bo)

MAX_MSG_LEN = 36  # section 2.2
ADDRESS_MASK = hti(b"\xF8")  # section 2.3 - top five bits of address are actually address
COMMAND_MASK = hti(b"\x07")  # section 2.3 - bottom three bits are command
# Address of each device (section 2.2")
ADDRESS_VMC = hti(b"\x00")
ADDRESS_CHANGER = hti(b"\x08")
ADDRESS_CD1 = hti(b"\x10")  # Cashless Device 1
ADDRESS_GATEWAY = hti(b"\x18")  # Communication Gateway
ADDRESS_DISPLAY = hti(b"\x20")
ADDRESS_EMS = hti(b"\x28")  # Energy Management System
ADDRESS_VALIDATOR = hti(b"\x30")  # Bill Validator
ADDRESS_USD1 = hti(b"\x40")  # Universal satellite device 1
ADDRESS_USD2 = hti(b"\x48")  # Universal satellite device 2
ADDRESS_USD3 = hti(b"\x50")  # Universal satellite device 3
ADDRESS_COIN1 = hti(b"\x58")  # Coin Hopper 1
ADDRESS_CD2 = hti(b"\x60")  # Cashless Device 2
ADDRESS_AVD = hti(b"\x68")  # Age Verification Device
ADDRESS_COIN2 = hti(b"\x70")  # Coin Hopper 2
# higher addresses are for future expansion
# section 2.2
MSG_ACK = b"\x00"  # ack
MSG_RET = b"\xAA"  # please retransmit last byte
MSG_NAK = b"\xFF"  # negative ack
BYTE_ORDER = "big"
CLIENT_ID = ""
cpuid = '100000002c5baf5a'
latest_raw_message = ''
last_price = 0
allow_api = True  # for debug make it False
api_max_retries = 10
# LOGGING/PRINT
LOG_EVERYTHING = 1
LOG_MEDIUM = 2
LOG_IMPORTANT = 3
LOG_NONE = 4
PRINT_LEVEL = LOG_IMPORTANT


def initialize_cpuid():
    # Extract serial from cpuinfo file
    global cpuid
    cpuid = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuid = line[10:26]
        f.close()
    except:
        cpuid = "ERROR000000000"
    return cpuid