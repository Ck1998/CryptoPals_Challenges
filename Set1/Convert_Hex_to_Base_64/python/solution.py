#!/usr/bin/env python3
# __author__ = "Chetanya Kunndra"
# This file is a solution file for Cryptopals Challenge Set 1
# Convert hex to base64
#
#
# imports
from base64 import encodestring

def decode_str(encoded_str):
    raw_str = bytes.fromhex(encoded_str).rstrip("\n")
    decoded_str = encodestring(raw_str)
    return decoded_str.decode("utf-8")


def validate_str(decoded_str:str):
    
    expected_answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    if expected_answer == decode_str:
        print("Correct Solution")
    else:
        print("Incorrect Solution")


if __name__ == "__main__":

    encoded_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    decoded_str = decode_str(encoded_str=encoded_str)
    validate_str(decoded_str=decoded_str)