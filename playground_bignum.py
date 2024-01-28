from bignum.bignum import bignum

if __name__ == '__main__':
    b = bignum("1234567890")
    print(b.shift_decimals_left(3))
    print(bignum('-043.4000').filtered())