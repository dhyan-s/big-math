from bignum.bignum import bignum
from bignum.operations.mul import Multiply, mul
from bignum.tester import Tester, InputValues, NumProperties

if __name__ == '__main__':
    tester = Tester('multiply', mul)
    
    # ______________________________________________________________________
    # Multiply.chunk_size = 3 # For testing small calculations
    # tester.test_random(5000, input_values=InputValues(no_of_values=3, input_type=NumProperties(max_whole_no_len=5, max_decimal_len=4, decimal=None, negative=None)))
    # ______________________________________________________________________
    
    # ______________________________________________________________________
    # Test speed with large inputs. Output file is stored in user_directory/.large_values.txt
    tester.test_in_file(num1_properties=NumProperties(whole_no_len=100000), 
                        num2_properties=NumProperties(whole_no_len=100000), 
                        write_result_in_file=[True, True],
                        use_existing_num=False)
    # ______________________________________________________________________