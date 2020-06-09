#!/usr/bin/env python3
# __author__ = "Chetanya Kunndra"
# This file is a solution file for Cryptopals Challenge Set 1
# Convert hex string - 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# to b64 string - SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

# imports
from base64 import encodebytes

# Main Logic
def decode_str(encoded_str):
    raw_str = bytes.fromhex(encoded_str)
    decoded_str = encodebytes(raw_str)
    return decoded_str.decode("utf-8")


def validate_str(decoded_str:str):
    
    expected_answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    if expected_answer == decoded_str:
        print("Correct Solution\n - ")
        print("Expected String - '"+expected_answer+"'")
        print("Decoded String - '"+decoded_str+"'")
    else:
        print("Incorrect Solution\n")
        print("Expected String - '"+expected_answer+"'")
        print("Decoded String - '"+decoded_str+"'")


if __name__ == "__main__":

    encoded_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print("String to convert - '"+encoded_str+"'\n")
    decoded_str = decode_str(encoded_str=encoded_str)
    decoded_str = decoded_str.rstrip("\n")
    validate_str(decoded_str=decoded_str)