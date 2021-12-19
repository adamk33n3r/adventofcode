import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node
from math import prod

USE_EXAMPLE = False
PRINT_DEBUG = False

class BytesHandler:
    def __init__(self, file):
        hexIn = file.readline()
        bits = bytes.fromhex(hexIn)
        binary = ''
        for byte in bits:
            binary += ('{0:08b}'.format(byte))
        self.bits = binary
        self.pos = 0

    def getvalue(self, numBits):
        ret = int(self.bits[self.pos:self.pos + numBits], 2)
        self.pos += numBits
        return ret
    def getpacket(self):
        version = self.getvalue(3)
        typeID = self.getvalue(3)
        data = self.getpacketdata(typeID)
        return version, typeID, data
    def getvaluepacket(self):
        value = 0
        segment = 0b10000
        while segment & 0b10000:
            segment = self.getvalue(5)
            value <<= 4
            value += segment & 0b1111
        return value
    def getpacketdata(self, typeID):
        if typeID == 4:
            return self.getvaluepacket()
        return self.getoperatorpacket()
    def getoperatorpacket(self):
        lengthTypeID = self.getvalue(1)
        if lengthTypeID == 1:
            return self.getpackets(self.getvalue(11))
        return self.getpacketsbylen(self.getvalue(15))
    def getpackets(self, num):
        return [self.getpacket() for i in range(num)]
    def getpacketsbylen(self, len):
        pos = self.pos + len
        ret = []
        while self.pos < pos:
            ret.append(self.getpacket())
        return ret

def dumppackethelper(packet, indent):
    version, typeID, data = packet
    print('\t'*indent + 'v: {}, id: {}'.format(version, typeID))
    if typeID == 4:
        print('\t'*(indent+1)+'value:', data)
    else:
        for sub in data:
            dumppackethelper(sub, indent + 1)
def dumppackets(root):
    dumppackethelper(root, 0)

def sumversions(packet):
    version, typeID, data = packet
    if typeID == 4:
        return version
    else:
        for sub in data:
            version += sumversions(sub)
        return version
    
def process(packet):
    version, typeID, data = packet
    if typeID == 4:
        return data
    
    if typeID == 0:
        return sum([process(sub) for sub in data])
    elif typeID == 1:
        return prod([process(sub) for sub in data])
    elif typeID == 2:
        return min([process(sub) for sub in data])
    elif typeID == 3:
        return max([process(sub) for sub in data])
    elif typeID == 5:
        return 1 if process(data[0]) > process(data[1]) else 0
    elif typeID == 6:
        return 1 if process(data[0]) < process(data[1]) else 0
    elif typeID == 7:
        return 1 if process(data[0]) == process(data[1]) else 0

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    bh = BytesHandler(file)
    root = bh.getpacket()
    # dumppackets(root)
    print(sumversions(root))

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    bh = BytesHandler(file)
    root = bh.getpacket()
    print(process(root))
