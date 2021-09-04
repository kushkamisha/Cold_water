from cold_water import Cold_water


def main():
    # Input data.
    N = int(input('Enter number of appliances: '))
    X = float(input('Enter X (from 4 to 8): '))

    my_water = Cold_water(N, X)
    my_water.predict()
    my_water.visualize_function()


if __name__ == '__main__':
    main()
