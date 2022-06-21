#!/usr/bin/python
from common import *

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
type_RR = ["ADD", "ADC", "SUB", "AND", "OR", "XOR", "CMP", "MOV"]
type_RM = ["STR", "LOAD"]
type_M = ["JMP", "JC", "JZ", "JN"]
type_R = ["INC", "DEC"]
type_RS = ["SHR", "SHL"]
type_RI = ["SET"]
def_DB = ["DB"]

opcodes = {
    "ADD": 1,
    "ADC": 2,
    "SUB": 3,
    "AND": 4,
    "OR": 5,
    "XOR": 6,
    "CMP": 7,
    "MOV": 8,
    "STR": 16,
    "LOAD": 17,
    "STRr": 18,
    "LOADr": 19,
    "JMP": 20,
    "JC": 21,
    "JZ": 22,
    "JN": 23,
    "INC": 24,
    "DEC": 25,
    "SHR": 26,
    "SHL": 27,
    "SET": 31,
}
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Nuevas instrucciones
type_R += ["SIG", "NEG"]
type_RR += ["MIX"]
type_M += ["CALL"]
type_NOARGS = ["RET"]
opcodes.update({
    "SIG": 9,
    "NEG": 10,
    "MIX": 11,
    "CALL": 12,
    "RET": 13,
})

if __name__ == '__main__':
    assembly(
        {
            "type_RR": type_RR,
            "type_RM": type_RM,
            "type_M": type_M,
            "type_R": type_R,
            "type_RS": type_RS,
            "type_RI": type_RI,
            "type_NOARGS": type_NOARGS,
            "def_DB": def_DB,
        }, opcodes)
