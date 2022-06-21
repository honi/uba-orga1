#!/usr/bin/python

from common import buildMicroOps

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Build micro operations constants

signals = {
    "RB_enIn": 0,
    "RB_enOut": 1,
    "RB_selectIndexIn": 2,
    "RB_selectIndexOut": 3,
    "MM_enOut": 4,
    "MM_load": 5,
    "MM_enAddr": 6,
    "RESERVED07": 7,
    "ALU_enA": 8,
    "ALU_enB": 9,
    "ALU_enOut": 10,
    "ALU_opW": 11,
    "ALU_OP": 12,
    "RESERVED_ALU_OP_1": 13,
    "RESERVED_ALU_OP_2": 14,
    "RESERVED_ALU_OP_3": 15,
    "JC_microOp": 16,
    "JZ_microOp": 17,
    "JN_microOp": 18,
    "RESERVED19": 19,
    "PC_load": 20,
    "PC_inc": 21,
    "PC_enOut": 22,
    "RESERVED23": 23,
    "DE_enOutImm": 24,
    "DE_loadL": 25,
    "DE_loadH": 26,
    "RESERVED27": 27,
    "RESERVED28": 28,
    "RESERVED29": 29,
    "load_microOp": 30,
    "reset_microOp": 31
}

ALUops = {
    "RESERVED0": 0,
    "ADD": 1,
    "ADC": 2,
    "SUB": 3,
    "AND": 4,
    "OR": 5,
    "XOR": 6,
    "CMP": 7,
    "SHR": 8,
    "SHL": 9,
    "RESERVED10": 10,
    "MIX": 11,
    "cte0x00": 12,
    "cte0x01": 13,
    "cte0x02": 14,
    "cte0xFF": 15
}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    buildMicroOps(signals, ALUops)
