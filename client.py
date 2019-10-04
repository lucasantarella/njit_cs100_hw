#! /usr/bin/env python3
# Echo Client

# Christopher Simon
# CS558
# Section 003

import time
import sys
import socket
import random
import struct

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
hostName = sys.argv[3]


def unpack_data(fmt, data):
    size = struct.calcsize(fmt)
    return struct.unpack(fmt, data[:size]), data[size:]


"""
Ask for A IN for the hostname
"""
question = hostName + " A IN"

returnTime = []
messageId = random.randint(1, 101)
returnCode = 0
answerLength = 0
messageType = 1
questionLength = len(question)

packed_data = struct.pack("hhihh%ds%ds" % (questionLength, answerLength), messageType, returnCode, messageId,
                          questionLength, answerLength,
                          question.encode(), ''.encode(), )

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Setting time out for request
clientsocket.settimeout(1)

i = 5
k = 0

# Send data to server
i = i - 1
k = k + 1
start = time.time()
print("Sending Request to " + str(host) + ", " + str(port) + ":")
print("Message ID: " + str(messageId))
print("Question Length: " + str(questionLength) + " bytes")
print("Answer Length: 0")  # no answer since this is a request
print("Question: " + str(question))
print("\n")
clientsocket.sendto(packed_data, (host, port))
# Receive the server response
try:
    dataEcho, address = clientsocket.recvfrom(1024)
    packet = unpack_data("hhihh", dataEcho)
    responseMessageType, responseReturnCode, responseMessageId, responseQuestionLength, responseAnswerLength = \
        packet[0]  # get vars from packet
    questionAndAnswer = packet[len(packet) - 1].decode()
    question = questionAndAnswer[:questionLength]
    answer = questionAndAnswer[questionLength:]

    if responseReturnCode == 0:
        statusString = "(No errors)"
    else:
        statusString = "(Name does not exist)"

    print("Received Response from " + host + str(port))
    print("Return Code: " + str(responseReturnCode) + " " + statusString)
    print("Message ID: " + str(responseMessageId))
    print("Question Length: " + str(responseQuestionLength))
    print("Answer Length: " + str(responseAnswerLength))
    print("Question: " + str(question))
    print("Answer: " + str(answer))

except socket.timeout:
    i = 1
    while i <= 3:
        print("Request timed out ...")
        clientsocket.sendto(packed_data, (host, port))
        print("Sending request to: " + str(host) + str(port))
        i = i + 1
    if i == 3:
        print("Request time out ... Exiting Program")
        exit(0)

# Close the client socket
clientsocket.close()
