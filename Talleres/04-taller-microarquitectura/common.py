#!/usr/bin/python

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#01 ADD  00001 XXXYYY-----
#02 ADC  00010 XXXYYY-----
#03 SUB  00011 XXXYYY-----
#04 AND  00100 XXXYYY-----
#05 OR   00101 XXXYYY-----
#06 XOR  00110 XXXYYY-----
#07 CMP  00111 XXXYYY-----
#08 MOV  01000 XXXYYY-----

#16 STR  10000 XXXMMMMMMMM
#17 LOAD 10001 XXXMMMMMMMM

#20 JMP  10100 ---MMMMMMMM
#21 JC   10101 ---MMMMMMMM
#22 JZ   10110 ---MMMMMMMM
#23 JN   10111 ---MMMMMMMM

#24 INC  11000 XXX--------
#25 DEC  11001 XXX--------
#26 SHR  11010 XXXYYY-----
#27 SHL  11011 XXXYYY-----

#31 SET  11111 XXXIIIIIIII

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from __future__ import print_function

import sys
import os

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Tokenize function


def tokenizator(filename):
    tokens = []
    newline = ['\n']
    comment = [';']
    blank = [' ', '\t'] + newline + comment
    reserve = ['[', ']', ',', ':']

    with open(filename) as f:
        line = []
        word = ""
        isComment = False
        while True:
            c = f.read(1)
            if not c:
                break

            if not isComment:

                if c in blank:
                    if len(word) > 0:
                        line = line + [word]
                    word = ""
                    if c in newline or c in comment:
                        if len(line) > 0:
                            tokens = tokens + [line]
                        line = []
                    if c in comment:
                        isComment = True

                elif c in reserve:
                    if len(word) > 0:
                        line = line + [word]
                    word = ""
                    line = line + [c]

                else:
                    word = word + c

            else:  # isComment
                if c in newline:
                    isComment = False
    return tokens


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Assembly code functions


def assembly(types, opcodes):
        if len(sys.argv) != 2:
            print("Usage: assembler.py file.asm")
            exit(1)

        filename = sys.argv[1]

        if filename[-4:] == ".asm":
            output = filename[:-4] + ".mem"
            outputH = filename[:-4] + ".txt"
        else:
            output = filename + ".mem"
            outputH = filename[:-4] + ".txt"

        tokens = tokenizator(filename)
        instructions, labels = removeLabels(tokens, types)
        parseBytes, parseHuman = parseInstructions(instructions, labels, types, opcodes)
        if parseBytes != None:
            printCode(output, parseBytes)
        if parseHuman != None:
            printHuman(outputH, parseHuman, labels, filename)


def removeLabels(tokens, types):
    instCount = 0
    reserveLabel = ':'
    instructions = []
    labels = {}
    for t in tokens:
        if len(t) > 1 and t[1] == reserveLabel:
            labels[t[0]] = instCount
            if len(t) > 2:
                instructions = instructions + [t[2:]]
                if t[2] in types["def_DB"]:
                    instCount = instCount + 1
                else:
                    instCount = instCount + 2
        else:
            instructions = instructions + [t[0:]]
            if t[0] in types["def_DB"]:
                instCount = instCount + 1
            else:
                instCount = instCount + 2
    return instructions, labels


def reg2num(reg):
    if reg[0] == "R":
        try:
            val = int(reg[1:])
        except ValueError:
            print("Error: Can not convert \"" + reg + "\"")
            return None
        if 0 <= val and val <= 7:
            return val
        print("Error: \"" + reg + "\" out of range (0-7)")
        raise ValueError()
    else:
        print("Error: \"" + reg + "\" is not a valid register")
        raise ValueError()


def mem2num(mem, labels):
    if mem in labels.keys():
        return labels[mem]
    else:
        try:
            if mem[0:2] == "0x" or mem[0:2] == "0X":
                val = int(mem[2:], 16)
            elif mem[-1:] == "b":
                val = int(mem[:-1], 2)
            else:
                val = int(mem, 10)
        except ValueError:
            print("Error: Can not convert \"" + mem + "\"")
            return None
        if 0 <= val and val <= 255:
            return val
        print("Error: \"" + mem + "\" out of range (0-255)")
        raise ValueError()


def shf2num(num):
    val = mem2num(num, {})
    if 0 <= val and val <= 7:
        return val
    print("Error: \"" + num + "\" out of range (0-7)")
    raise ValueError()


def buidInst(d):
    n = 0
    if "O" in d:
        n = n + (d["O"] << 11)
    if "X" in d:
        n = n + (d["X"] << 8)
    if "Y" in d:
        n = n + (d["Y"] << 5)
    if "M" in d:
        n = n + (d["M"])
    if "I" in d:
        n = n + (d["M"])
    return n


def appendParse(parseBytes, parseHuman, i, n):
    addr = len(parseBytes)
    parseBytes.append(n >> 8)
    parseBytes.append(n & 0xFF)
    parseHuman.append([addr, i])


def parseInstructions(instructions, labels, types, opcodes):
    parseBytes = []
    parseHuman = []
    for i in instructions:
        try:
            # AAA Rx,Ry || Rx <= Rx AAA Ry
            if i[0] in types["type_RR"]:
                if i[2] == ",":
                    n = buidInst({
                        "O": opcodes[i[0]],
                        "X": reg2num(i[1]),
                        "Y": reg2num(i[3])
                    })
                    appendParse(parseBytes, parseHuman, i, n)
                else:
                    raise ValueError("Error: Invalid instruction \"" + i[0] +
                                     "\"")
                    break
            # STR || LOAD
            elif i[0] in types["type_RM"]:
                if i[0] == "STR" and i[1] == "[" and i[3] == "]" and i[
                        4] == ",":
                    if i[2][0] == "R":
                        # STR [Rx],RY  || [Rx] <= Ry
                        n = buidInst({
                            "O": opcodes[i[0] + 'r'],
                            "X": reg2num(i[2]),
                            "Y": reg2num(i[5])
                        })
                    else:
                        # STR [M],Rx  || [M] <= Rx
                        n = buidInst({
                            "O": opcodes[i[0]],
                            "X": reg2num(i[5]),
                            "M": mem2num(i[2], labels)
                        })
                    appendParse(parseBytes, parseHuman, i, n)
                elif i[0] == "LOAD" and i[2] == "," and i[3] == "[" and i[
                        5] == "]":
                    if i[4][0] == "R":
                        # LOAD Rx,[Ry] || Rx <= [Ry]
                        n = buidInst({
                            "O": opcodes[i[0] + 'r'],
                            "X": reg2num(i[1]),
                            "Y": reg2num(i[4])
                        })
                    else:
                        # LOAD Rx,[M] || Rx <= [M]
                        n = buidInst({
                            "O": opcodes[i[0]],
                            "X": reg2num(i[1]),
                            "M": mem2num(i[4], labels)
                        })
                    appendParse(parseBytes, parseHuman, i, n)
                else:
                    raise ValueError("Error: Invalid instruction \"" + i[0] +
                                     "\"")
                    break
            # Jxx M
            elif i[0] in types["type_M"]:
                n = buidInst({"O": opcodes[i[0]], "M": mem2num(i[1], labels)})
                appendParse(parseBytes, parseHuman, i, n)
            # AAA Rx
            elif i[0] in types["type_R"]:
                n = buidInst({"O": opcodes[i[0]], "X": reg2num(i[1])})
                appendParse(parseBytes, parseHuman, i, n)
            # SSS Rx,7
            elif i[0] in types["type_RS"]:
                if i[2] == ",":
                    n = buidInst({
                        "O": opcodes[i[0]],
                        "X": reg2num(i[1]),
                        "Y": shf2num(i[3])
                    })
                    appendParse(parseBytes, parseHuman, i, n)
                else:
                    raise ValueError("Error: Invalid instruction \"" + i[0] +
                                     "\"")
                    break
            # SET Rx, M
            elif i[0] in types["type_RI"]:
                if i[2] == ",":
                    n = buidInst({
                        "O": opcodes[i[0]],
                        "X": reg2num(i[1]),
                        "M": mem2num(i[3], labels)
                    })
                    appendParse(parseBytes, parseHuman, i, n)
                else:
                    raise ValueError("Error: Invalid instruction \"" + i[0] +
                                     "\"")
                    break
            # DB M
            elif i[0] in types["def_DB"]:
                parseHuman.append([len(parseBytes), i])
                parseBytes.append(mem2num(i[1], labels))

            # RET
            elif i[0] in types["type_NOARGS"]:
                n = buidInst({"O": opcodes[i[0]]})
                appendParse(parseBytes, parseHuman, i, n)

            ##
            else:
                raise ValueError("Error: Unknown instruction \"" + i[0] + "\"")
                sys.exit(1)

        except ValueError as err:
            if len(err.args) > 0:
                print(err.args[0])
            print("Error: Instruction: " + " ".join(i))
            sys.exit(1)

    return parseBytes, parseHuman


def printCode(output, parse):
    f = open(output, "w")
    f.write("v2.0 raw\n")
    for i in parse:
        f.write('%02x ' % i)
        f.write("\n")
    f.close()


def printHuman(outputH, parseHuman, labels, filename):
    f = open(outputH, "w")

    inverseLabels = {}
    for name, addr in labels.items():
        if addr in inverseLabels:
            inverseLabels[addr].append(name)
        else:
            inverseLabels[addr] = [name]

    allNames = list(map(lambda x: ", ".join(x), inverseLabels.values()))
    if len(allNames) == 0:
        maxName = 0
    else:
        maxName = max(map(len, allNames))

    for p in parseHuman:
        if p[0] in inverseLabels:
            f.write((", ".join(inverseLabels[p[0]])).rjust(maxName))
        else:
            f.write(" " * maxName)
        f.write(' |%02x| ' % p[0])
        f.write(" ".join(p[1]))
        f.write("\n")
    f.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Build micro operations functions


def buildMicroOps(signals, ALUops):
    if len(sys.argv) != 2:
        print("Usage: buildMicroOps.py file.ops")
        exit(1)

    filename = sys.argv[1]

    if filename[-4:] == ".ops":
        output = filename[:-4] + ".mem"
    else:
        output = filename + ".mem"

    tokens = tokenizator(filename)
    microCode = parseOpcodes(tokens, signals, ALUops)
    code = codeValues(microCode)
    printMicroCode(output, code)


def val2num(val, ALUops):
    if val in ALUops.keys():
        return ALUops[val]
    else:
        return int(val)


def str2signal(signal, signals, ALUops):
    sig = signal.split("=")
    if sig[0] in signals.keys():
        index = signals[sig[0]]
        if len(sig) > 1:
            num = val2num(sig[1], ALUops)
        else:
            num = 1
        return [index, num]
    else:
        print("Error: Signal \"" + signal + "\" unknown")
        sys.exit(1)


def parseOpcodes(tokens, signals, ALUops):
    microCode = []
    label = ""
    microInst = []
    for t in tokens:
        if len(t) > 1 and t[1] == ":":
            if not (len(microInst) == 0):
                microCode.append([label, microInst])
                microInst = []
            label = t[0]
        else:
            microInst.append(
                filter(lambda x: x != None,
                       map(lambda s: str2signal(s, signals, ALUops), t)))
    if not (len(microInst) == 0):
        microCode.append([label, microInst])
        microInst = []
    return microCode


def codeValues(microCode):
    code = {}
    for m in microCode:
        addr = int(m[0], 2)
        micro = []
        for step in m[1]:
            s = 0
            for sign in step:
                s = s + (sign[1] << sign[0])
            micro.append(s)
        code[addr] = micro
    return code


def printMicroCode(output, code):
    f = open(output, "w")
    f.write("v2.0 raw\n")
    for i in range(32):
        if i in code.keys():
            for m in code[i]:
                f.write('%08x' % m)
                f.write(" ")
            f.write(str(16 - len(code[i])) + "*0\n")
        else:
            f.write("80000000 15*0\n")
    f.close()
