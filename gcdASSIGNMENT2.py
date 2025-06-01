def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None
    if a == 0 and b == 0:
        print("Error: GCD is undefined for both inputs zero.")
        return None
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

print(gcd(54, 24))
print(gcd(48, 18))
print(gcd(101, 10))
