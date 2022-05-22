def xor(first, second):
    return bytearray(x^y for x,y in zip(first, second))

MSG = "This is a known message!"
HEX_1 = "a469b1c502c1cab966965e50425438e1bb1b5f9037a4c159"
HEX_2 = "bf73bcd3509299d566c35b5d450337e1bb175f903fafc159"
# Convert ascii/hex string to bytearray
D1 = bytes(MSG, 'utf-8')
D2 = bytearray.fromhex(HEX_1)
D3 = bytearray.fromhex(HEX_2)
r1 = xor(D1, D2)
r2 = xor(D2, D3)
r3 = xor(D2, D2)
r4 = xor (r1 , D3 )
print("*********************************************************************************")
print("MSG XOR HEX_1")
print(r1.hex())
print("𝑃 2 is ")
print(r4.decode("ASCII"))
print("\n*********************************************************************************")
print("HEX_1 XOR HEX_2")
print(r2.hex())
print("*********************************************************************************")
print("HEX_1 XOR HEX_1")
print(r3.hex())