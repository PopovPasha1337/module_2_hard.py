def ancient_cipher(n):
    result = ""
    for i in range(1, n):
        for j in range(i+1, n+1):
            if n % (i + j) == 0:
                result += f"{i} {j}"
    return result


for n in range(3,21):
 print(f"{n} - {ancient_cipher(n)}")