def imprimir_diamante(n):

    for i in range(n):
        print (" " * (n-1-i), end="")

        print("*", end="")

        if i > 0:
            print(" " *(2*i-1), end="")
            print("*", end="")

            for i in range(n-2, -1, -1):
                print(" "*(2*1-1), end="")
                print("*", end="")
                print()

    