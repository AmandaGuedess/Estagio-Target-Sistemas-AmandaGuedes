def inverter_string(s):
    invertida = ''
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    return invertida

string = "exemplo"
print(inverter_string(string))
