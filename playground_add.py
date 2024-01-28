from bignum.bignum import bignum
from bignum.operations.add import add, Add
from bignum.tester import Tester, InputValues, NumProperties


if __name__ == '__main__':
    tester = Tester('add', add)
    
    # ____________________________________________________________________
    Add.chunk_size = 3 # For testing purposes. comment out when not testing small numbers.
    tester.test_random(5000) # Test accuracy with randomly generated numbers
    # ______________________________________________________________________
    
    # ______________________________________________________________________
    # # Test speed with large inputs. Output file is stored in user_directory/.large_values.txt
    # tester.test_in_file(num1_properties=NumProperties(whole_no_len=1000000), 
    #                     num2_properties=NumProperties(whole_no_len=1000000), 
    #                     write_result_in_file=[True, True],
    #                     use_existing_num=False)
    # ______________________________________________________________________