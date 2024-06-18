# Harris Ransom
# PicoCTF - Mind Your Ps and Qs
# Category: Cryptography

def main():
    # Given values
    c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423 # Encrypted message (ciphertext)
    n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423 # Modulus, n = p*q
    e = 65537   # Public exponent
    
    # Factor n to get p and q (factordb)
    p = 1955175890537890492055221842734816092141
    q = 670577792467509699665091201633524389157003
    isValid = (p*q == n)
    if (isValid):
        print("p and q are valid")
    else:
        print("p and q are invalid")
        exit()

    # Calculate other RSA parameters
    d = pow(e, -1, (p-1)*(q-1)) # Private exponent
    m = pow(c, d, n) # Decrypted message (plaintext)

    # Print the decrypted message
    print(bytes.fromhex(hex(m)[2:]))

if __name__ == "__main__":
    main()
    