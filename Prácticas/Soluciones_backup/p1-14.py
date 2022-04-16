numbers = [0x7744, 0x5499, 0x6788, 0xAB68, 0x88BD, 0x9879, 0x0003]

for n in numbers:
    nb = bin(n)[2:].zfill(16)
    nb_str = ' '.join([nb[i:i+4] for i in range(0, len(nb), 4)])
    nd = int(nb, 2)
    if nb[0] == '1':
        nd = -2**16 + nd
    print(f'({nb_str})₂ = ({nd})₁₀')
