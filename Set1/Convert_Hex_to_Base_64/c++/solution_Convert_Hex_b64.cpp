// Cryptopals Challenge Set 1 - Change Hex to Base64
// Created By - Chetanya Kunndra
// Date - Oct 5 2020
// Time - 0010 IST

// Solution incomplete

#include<iostream>
#include<string>

using namespace std;

string convert_to_base64(string string_to_convert)
{
    string converted_string;

    return converted_string;
}


bool validate_result(string converted_string)
{
    string expected_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";

    return (expected_string==converted_string);
}

int main() 
{
    string problem_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
    string converted_string;

    converted_string = convert_to_base64(problem_string);

    if(validate_result(converted_string))
    {
        return 0;
    }
    else
    {
        return 1;
    }
    
}
