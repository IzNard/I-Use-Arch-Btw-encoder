TOKENS = ["i", "use", "arch", "btw"]

def encode(secret: str) -> str:
    encoded = []
    for ch in secret:
        n = ord(ch)
        digits = []
        while n > 0:
            digits.append(TOKENS[n % 4])
            n //= 4
        encoded.append(" ".join(reversed(digits)))
    return " | ".join(encoded)

def decode(encoded: str) -> str:
    decoded = []
    reverse = {t: i for i, t in enumerate(TOKENS)}
    for block in encoded.split(" | "):
        n = 0
        for word in block.split():
            n = n * 4 + reverse[word]
        decoded.append(chr(n))
    return "".join(decoded)

def main():
    print("i use arch btw secret hider")
    choice = input("Do you want to (e)ncode or (d)ecode? ").strip().lower()
    if choice in ("e", "encode"):
        text = input("Enter normal text: ")
        print("\nArchified output:\n")
        print(encode(text))
    elif choice in ("d", "decode"):
        text = input("Enter archified string: ")
        print("\nDecoded output:\n")
        print(decode(text))
    else:
        print("Invalid option, btw.")

if __name__ == "__main__":
    main()
