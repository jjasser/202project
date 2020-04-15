import string
import re
from itertools import islice
import codecs
import binascii
from pytlv.TLV import *

with open("SCFFile.tlv", "rb") as files:
    in_bytes = files.read()
    #print("Please enter a tag value:")
   # tag = input()
   # print("The users has entered %b" % tag)
   # print("Please enter an end tag value")
    #end_tag = input()
    #print("The user has entered %b" % end_tag)
    start = in_bytes.find(b"\x04\x00")
    end = in_bytes.find(b"\x00\x05")

    accumulate = ''
    for i in range(start, end):
        accumulate += str(chr(in_bytes[i]))
        print(accumulate)
    cert_name = accumulate.split("=")[1].split(";")[0]
    print(cert_name)

    # print(cert_name)
    # tlv = TLV(['9f22'])
    # print(tlv.parse(str(in_bytes)))
    # print(str(in_bytes).split("\\"))
    # in_ascii = binascii.b2a_uu(in_bytes)
    # for i in in_ascii:
    #    print(in_ascii)
    # print(in_bytes)
    # hex_bytes = binascii.hexlify(in_bytes)
    # print(hex_bytes)



    #for lines in files:
        # word = lines.decode(encoding="hex_codec", errors="ignore")
        # print(word)
        # for secondline in words:
        #   print(str(secondline).split(";"))
        # print(str(lines).split(";"))

        # print(lines.decode("utf-8", errors="ignore"))
        # print(str(lines).split("\\"))
        # if str(lines).find("CN"):
        # print(str(lines).split(";"))
        # print("\n")
        # print(type)
