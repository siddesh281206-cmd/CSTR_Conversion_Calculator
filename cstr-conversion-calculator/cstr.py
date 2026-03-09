def calculate_conversion(k, tau):
    """
    Calculate conversion for a first-order reaction in a CSTR
    """
    X = (k * tau) / (1 + k * tau)
    return X


def main():
    print("CSTR Conversion Calculator")

    k = float(input("Enter reaction rate constant (k): "))
    tau = float(input("Enter residence time (tau): "))

    conversion = calculate_conversion(k, tau)

    print("Conversion of reactant =", round(conversion, 4))


if __name__ == "__main__":
    main()