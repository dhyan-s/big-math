
from bignum.bignum import bignum
from bignum.operations.sub import Subtract, sub
from bignum.tester import Tester, InputValues, NumProperties

if __name__ == '__main__':
    tester = Tester('sub', sub)
    
    # ______________________________________________________________________
    # Subtract.chunk_size = 3
    # tester.test_random(5000)
    # ______________________________________________________________________
    
    # ______________________________________________________________________
    # # Test speed with large inputs. Output file is stored in user_directory/.large_values.txt
    tester.test_in_file(num1_properties=NumProperties(whole_no_len=1000000), 
                        num2_properties=NumProperties(whole_no_len=1000000), 
                        write_result_in_file=[True, True],
                        use_existing_num=False)
    # ______________________________________________________________________
    