from typing import List, Dict

from ..bignum import bignum
from .add import add, Add


class Multiply:
    chunk_size = 2145
    
    def __add_value_to_addition_slots(self, value, addition_slots: Dict[int, List[str]], slot_id: int) -> None:
        if slot_id not in addition_slots:
            addition_slots[slot_id] = []
        addition_slots[slot_id].append(value)
        
    
    def results_addition_chunking(self, chunk_results: List) -> bignum:
        addition_slots = {}
        for idx, chunk_result in enumerate(chunk_results):
            starting_slot_no = idx
            chunks_of_chunk_res = bignum(chunk_result).chunk_whole(chunk_size=Multiply.chunk_size, reverse=True)
            for idx, chunk in enumerate(chunks_of_chunk_res):
                self.__add_value_to_addition_slots(chunk.rjust(Multiply.chunk_size, '0'), addition_slots, starting_slot_no+idx)
                
        carry = 0
        slot_addition_results = []
        for slot in sorted(list(addition_slots.keys())):
            res, carry = Add.result_and_carry(*addition_slots[slot], carry)
            slot_addition_results.append(res)
            
        slot_addition_results.reverse()
        if carry > 0:
            slot_addition_results[0] = f"1{slot_addition_results[0]}"
            
        for idx in range(len(slot_addition_results)):
            slot_addition_results[idx] = str(slot_addition_results[idx].rjust(Multiply.chunk_size, '0'))
            
        result = ''.join(slot_addition_results)
        return bignum(result)
    
    def mul_two_whole_nums(self, num1: bignum, num2: bignum) -> bignum:
        if len(num1) <= Multiply.chunk_size and len(num2) <= Multiply.chunk_size:
            return bignum(int(num1) * int(num2))
        
        num1_chunks = list(num1.chunk_whole(Multiply.chunk_size, reverse=True))
        num2_chunks = list(num2.chunk_whole(Multiply.chunk_size, reverse=True))
        
        overall_chunk_results = []
        
        for num2_chunk in num2_chunks:
            chunk_results = []
            for num1_chunk in num1_chunks:
                res = bignum(int(num1_chunk) * int(num2_chunk))
                chunk_results.append(res)
            overall_chunk_results.append(self.results_addition_chunking(chunk_results))
        overall_result = self.results_addition_chunking(overall_chunk_results)
        return overall_result.filtered()
                
    
    def mul_two_positive_nums(self, num1: bignum, num2: bignum) -> bignum:
        """Calculate the product of two positive numbers."""
        
        # Filter out leading and trailing zero's to save computation
        num1, num2 = num1.filtered(), num2.filtered()
        total_decimal_length = len(str(num1.get_decimal()).rstrip('0') + str(num2.get_decimal()).rstrip('0'))
        num1, num2 = num1.remove_decimal(), num2.remove_decimal()
        num1, num2 = num1.filtered(), num2.filtered()
        res = self.mul_two_whole_nums(num1, num2)
        res = res.shift_decimals_left(total_decimal_length)
        return res
    
    def mul_two_nums(self, num1: bignum, num2: bignum) -> bignum:
        """Calculate the product of two numbers."""
        if num1 == '0' or num2 == '0':
            return bignum('0')
        neg_res = not ((num1.is_positive() and num2.is_positive()) or (num1.is_negative() and num2.is_negative()))
        res = self.mul_two_positive_nums(num1.to_positive(), num2.to_positive())
        res = res.to_negative() if neg_res else res
        return res
    
    def mul(self, *args) -> bignum:
        """Calculate the product of the given numbers."""
        if not args: 
            return bignum('0')
        final_result = bignum(args[0])
        for item in args[1:]:
            final_result = self.mul_two_nums(final_result, bignum(item))
        return final_result
    

mul = Multiply().mul
