#!/usr/bin/env python3
# __author__ = "Chetanya Kunndra"
# This file is a solution file for Cryptopals Challenge Set 1
# Convert hex string - 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# to b64 string - SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
# Shorter version of solution_Convert_Hex_to_b64.py

# imports
from base64 import encodebytes

# Only Logic
encoded_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
converted_str = encodebytes(bytes.fromhex(encoded_str)).decode("utf-8").rstrip("\n")
# OR
# converted_str = encodebytes(bytes.fromhex('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')).decode("utf-8").rstrip("\n")

print("Encoded String: "+encoded_str)

print("Converted String: "+converted_str)
