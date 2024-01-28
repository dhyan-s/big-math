from decimal import getcontext
from typing import Tuple

from ..bignum import bignum
from .add import add
from .sub import sub
from .mul import mul

class Divide:
    chunk_size = 2145
    prec = 100
    
    def __floor_div_before_10(self, num1: bignum, num2: bignum) -> bignum:
        for i in range(0, 10):
            res = mul(num2, i)
            if res > num1:
                return bignum(i-1)  
            
    # def div_two_whole_nums(self, num1: bignum, num2: bignum) -> bignum:
    #     # Unfinished, out of time
    #     min_dividend_len = len(num2) + 1
    #     num1 = num1.ljust(min_dividend_len, '0')
    #     quotient = ""
    #     idx = len(num2)-1
    #     remainder = num1[:idx+1]
    #     decimal = False
    #     while (remainder != '0' or idx < len(num1)) and len(bignum(quotient).get_decimal()) <= Divide.prec:
    #         quotient += str(self.__floor_div_before_10(remainder, num2))
    #         remainder -= mul(quotient[-1], num2)
    #         idx += 1
    #         if idx >= len(num1):
    #             if not decimal:
    #                 quotient += '.'
    #                 decimal = True
    #             num1 = bignum(str(num1) + '0')
    #         remainder = bignum(str(remainder) + str(num1[idx]))
    #     return bignum(quotient).filtered()
        
    def div_two_whole_nums(self, num1: bignum, num2: bignum) -> bignum:
        from decimal import Decimal, MAX_PREC, MAX_EMAX
        getcontext().prec = Divide.prec
        getcontext().Emax = MAX_EMAX
        return bignum(Decimal(str(num1)) / Decimal(str(num2)))
        
    
    def div_two_positive_nums(self, num1: bignum, num2: bignum) -> bignum:
        """Calculate the product of two positive numbers."""
        
        # Filter out leading and trailing zero's to save computation
        num1, num2 = num1.filtered(), num2.filtered()
        decimals_to_shift = len(str(num2.get_decimal()).rstrip('0')) - len(str(num1.get_decimal()).rstrip('0')) # Using rstrip because get_decimal(whole_no) returns '0'
        num1, num2 = num1.remove_decimal(), num2.remove_decimal()
        res = self.div_two_whole_nums(num1, num2)
        res = res.shift_decimals_left(decimals_to_shift)
        return res
    
    def div_two_nums(self, num1: bignum, num2: bignum) -> bignum:
        """Calculate the quotient of two numbers."""
        if num1 == '0':
            return bignum('0')
        if num2 == '0':
            raise ZeroDivisionError()
        neg_res = not ((num1.is_positive() and num2.is_positive()) or (num1.is_negative() and num2.is_negative()))
        res = self.div_two_positive_nums(num1.to_positive(), num2.to_positive())
        res = res.to_negative() if neg_res else res
        return res
    
    def div(self, *args: Tuple[bignum]) -> bignum:
        """Calculate the quotient of the given numbers."""
        if not args: 
            return bignum('0')
        final_result = bignum(args[0])
        for item in args[1:]:
            final_result = self.div_two_nums(final_result, bignum(item))
        return final_result
    
    
div = Divide().div