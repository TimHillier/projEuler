#https://projecteuler.net/problem=29


def IntCombs(a,b):
    products = []
    for A in range(2,a+1):
        for B in range(2,b+1):
            products.append(A**B)
    ProductSet = set(products)
    print(len(ProductSet))

def main():
    IntCombs(100,100)

main()