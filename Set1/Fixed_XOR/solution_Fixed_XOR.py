#!/usr/bin/env python3
# __author__ = "Chetanya Kunndra"
# This file is a solution file for Cryptopals Challenge Set 1 Challenge - Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination. 
# Inputs - 
#   1c0111001f010100061a024b53535009181c
#   1c0111001f010100061a024b53535009181c
# Output -
#   746865206b696420646f6e277420706c6179


def xor_inputs(input1, input2):
    raw_input_1 = bytes.fromhex(input1)
    raw_input_2 = bytes.fromhex(input2)
    xored_str =  ""
    
    for i in range(len(raw_input_1)):
        xored_str += str(raw_input_1[i]^raw_input_2[i])
    
    #xored_str = xored_str.hex()
    
    return xored_str


def validate_str(xor_output:str):
    
    expected_answer = "746865206b696420646f6e277420706c6179"
    if expected_answer == xor_output:
        print("Correct Solution\n")
        print("Expected String - '"+expected_answer+"'")
        print("Decoded String - '"+xor_output+"'")
    else:
        print("Incorrect Solution\n")
        print("Expected String - '"+expected_answer+"'")
        print("Decoded String - '"+xor_output+"'")


if __name__ == "__main__":

    input1 = "1c0111001f010100061a024b53535009181c"
    input2 = "686974207468652062756c6c277320657965"
    xor_output = xor_inputs(input1=input1, input2=input2)
    validate_str(xor_output=xor_output)