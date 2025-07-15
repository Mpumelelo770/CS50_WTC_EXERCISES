def main():
    m = int(input("Enter the mass: "))
    print(energy(m))

def energy(m):
    c = 300000000
    E = m*c**2
    return E

main()