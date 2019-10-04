#! /usr/bin/env python3
# Echo Server

# Christopher Simon
# CS558
# Section 003


import os
import random
import socket
import struct
import sys


def unpack_data(fmt, data):
    size = struct.calcsize(fmt)
    return struct.unpack(fmt, data[:size]), data[size:]


valuesForDictionary = ''
keyForDictionary: str = ''
stringSub = ''
subOfStringOfSub: str = ''
dictionaryForDnsFile = {}
# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
newSub = ''

# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))
print('The server is ready to receive on port: ' + str(serverPort) + "\n")

# Opening textfile to read from
dnsMasterFile = open(os.getcwd() + '/dns-master.txt', 'r')
dnsMasterFile.seek(0)
lines = dnsMasterFile.readlines()
for sub in lines:
    if "#" not in sub:
        if sub[0] != "\n":
            stringSub = sub.split()
            answer = sub.rstrip('\n')
            newSub = stringSub[0] + " " + stringSub[1] + " " + stringSub[2]
            dictionaryForDnsFile.update({newSub: answer})
            print(answer)


def unpack_data(fmt, data):
    size = struct.calcsize(fmt)
    return struct.unpack(fmt, data[:size]), data[size:]


# loop forever listening for incoming UDP messages
while True:
    # Receive and print the client data from "data" socket
    data, address = serverSocket.recvfrom(1024)
    packet = unpack_data("hhihh", data)
    messageType, returnCode, messageId, questionLength, answerLength = packet[0]  # get vars from packet
    question = packet[len(packet) - 1].decode()

    print("Responding to ping request with sequence number " + str(messageId))

    if question in dictionaryForDnsFile.keys():
        # have key, respond yes
        print("Responding to client " + address[0] + ", " + str(address[1]))
        answer = dictionaryForDnsFile[question]
        answerLength = len(answer)
        response = struct.pack("hhihh%ds%ds" % (questionLength, answerLength,), 2, 0, messageId, 0,
                               answerLength, question.encode(), answer.encode())
        serverSocket.sendto(response, address)
    else:
        # no key, respond yes
        print("Responding to client " + address[0] + ", " + str(address[1]))
        answerLength = len(answer)
        response = struct.pack("hhihh%ds%ds" % (questionLength, answerLength,), 2, 1, messageId, 0,
                               answerLength, question.encode(), ''.encode())
        serverSocket.sendto(response, address)
