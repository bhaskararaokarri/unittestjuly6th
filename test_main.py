"""
@ Bhaskara Rao Karri,
Date : 06/07/2020.
"""
# Import the required Modules on here.
import unittest
import logging
import warnings
from main import add,lenght_function,raise_function,isZero,grtaer_function,less_function,Test,Test1,collection_function,float_equal,dict_function,count_function,membership_in_function,membership_notin_function,count_equall_function

""" 
Define a ExampleTest class on here  and that calss inheritance a TestCase class from Unittest Module. 
and this ExampleTest class define so many testcase functions and checking the all testcases show the Output in form of testcases 
testcasee Success.
"""
class ExampleTest(unittest.TestCase):
    def test_sum_list(self):
        # assertEqual()- Tests that the two arguments are equal in value.
        self.assertEqual(add([1,4,3]),8,"sum is 8 only")
    
    def test_sum_tuple(self):
        # assertEqual()- Tests that the two arguments are equal in value.
        self.assertEqual(add((1,4,7)),12,"sum is 12 only")

    def test_sum(self):
        # assertNotEqual()- Tests that the two arguments are unequal in value.
        self.assertNotEqual(add([4,7]),5,"sum should  not 11 only") 

    def test_len_list(self):
        # assertNotEquals()- Tests that the two arguments are unequal in value.
        self.assertNotEquals(6,lenght_function([2,6,5,4,6,2,8]),"sum should  not 8 only")

    
    def test_ex1(self):
        # assertAlmostEqual()- Tests that the first and second arguments have approximately equal values.
        self.assertAlmostEqual(float_equal(1.00000801),1.000008,6,True)

    def test_not_almost_equal(self):
        # assertNotAlmostEqual()- Tests that the first and second arguments do not have approximately equal values.
        self.assertNotAlmostEqual(float_equal(1.000008123),1.000049123,6,True)

    # depricated function
    def test_ex2(self):
        # assertAlmostEqual()- Tests that the first and second arguments have approximately equal values.
        self.assertAlmostEquals(float_equal(0.12345999), 0.123459944, 6, 0.00001)

    def test_grater(self):
        # assertGreater()- Tests that the first argument is greater than the second.
        self.assertGreater(grtaer_function(8,4),6,True)

    def test_grtaer_equall(self):
        # assertGreaterEqual()- Tests that the first argument is greater than or equal to the second.
        self.assertGreaterEqual(grtaer_function(7,5),7,True)

    def test_less(self):
        # assertLess()- Tests that the first argument is lesser than the second.
        self.assertLess(less_function(6,10),8,True)

    def test_less_equall(self):
        # assertLessEqual()- Tests that the first argument is lesser than or equal to the second.   
        self.assertLessEqual(less_function(7,14),7,True)

    def test_list_equal(self):
        # assertListEqual()- Tests that two lists are equal.
        self.assertListEqual(collection_function([1,4,3]),[1,4,3],True)
    
    def test_tuple_equal(self):
        # assertTupleEqual()- Tests that two lists are equal.
        self.assertTupleEqual(collection_function(('a','b','c')),('a','b','c'),True)

    def test_set_equal(self):
        # assertSetEqual()- Tests that two sets are equal.
        self.assertSetEqual(collection_function({7,8,9}),{9,7,8},True)

    def test_dict_equal(self):
        # assertDictEqual()- Tests that two dictionaries are equal.
        dict1 = {'x':7,'y':8,'z':9}
        dict2 = {'x':7,'y':8,'z':9}
        self.assertDictEqual(dict_function(dict1),dict2,"both dictionaries are Equall")

    def test_sequence_equal(self):
        # assertSequenceEqual()- Tests that two sequences are equal.
        self.assertSequenceEqual(collection_function("bhaskar"),"bhaskar",True)

    def test_multilines_equal(self):
        # assertMultiLineEqual()- Tests that the first argument, which is a multiline string,
        #  is equal to the second.
        self.assertMultiLineEqual(collection_function("bhas\nkar"),"bhas\nkar",True)

    def test_dict_subset(self):
        # assertDictContainsSubset()-  Tests that the first first dictionary is a sub set of second dictionary.
        dict1 = {'x':4}
        dict2 ={'x':4,'c':3}
        self.assertDictContainsSubset(dict_function(dict1),dict2,True)

    def test_in(self):
        # assertIn()- Tests that the first argument is in the second.
        value1 = 5
        value2 = (1,2,5)
        self.assertIn(membership_in_function(value1,value2),value2,True)

    def test_not_in(self):
        # assertNotIn()- Tests that the first argument is not in the second.
        value1 = 4
        value2 = (1,2,5)
        self.assertNotIn(membership_notin_function(value1,value2),value2,True)

    def test_ex_list(self):
        # assertNotIn()- Tests that the first argument is not in the second.
        value1 = 5
        value2 = [1,2,3,4,6]
        self.assertNotIn(membership_notin_function(value1,value2),value2,False)

    def test_is(self):
        # assertIs()- Tests that the arguments evaluate to the same object.
        t1 = Test()
        t2 = t1
        self.assertIs(t1,t2,True)
    
    def test_is_not(self):
        # assertIsNot()- Tests that the arguments do not evaluate to the same object.
        t1 = Test()
        t2 = Test()
        self.assertIsNot(t1,t2,True)

    def test_is_instance(self):
        # assertIsInstance()- Tests that the first argument (object) is an instance of the second (class).
        t1 = Test()
        self.assertIsInstance(t1,Test,True)

    def test_is_not_instance(self):
        # assertNotIsInstance()- Tests that the first argument (object) is not an instance of the second (class).
        t1 = Test()
        self.assertNotIsInstance(t1,Test1,False)

    def test_equall(self):
        # assertEqual()- Tests that the two arguments are equal in value.
        self.assertEqual(count_function(3,1),4,True)
    
    def test_count_equal(self):
        # assertCountEqual()- Tests that the first argument, which is a sequence, 
        # contains the same as does the second.
        value1 =  (1,2,3,4)
        self.assertCountEqual(count_equall_function([1,2,3,4]),value1,True)

    def test_is_none(self):
        # assertIsNone()- Tests that the argument evaluates to none.
        # t1 = Test()
        t3 = None
        self.assertIsNone(t3,True)

    def test_is_not_none(self):
        # assertIsNotNone()- Tests that the argument does not evaluate to none.
        t1 = Test()
        self.assertIsNotNone(t1,True)

    def test_true(self):
        # assertTrue()- Tests that the argument has a Boolean value of True.
        t1 = Test()
        t2 = Test()
        self.assertTrue(t1 != t2,True)

    def test_false(self):
        # assertFalse()- Tests that the argument has a Boolean value of False.
        t1 = Test()
        t2 = Test()
        self.assertFalse(t1 == t2,True)

    def test_raise(self):
        # assertRaises()- Tests that Python raises an exception when we call the callable with positional/
        #  keyword arguments we also passed to this method.
        self.assertRaises(Exception,raise_function,100)

    def test_raise_regex(self):
        # assertRaisesRegex()- Tests that regex matches on the string representation of the exception raised; 
        # similar to assertRaises().
        self.assertRaisesRegex(Exception,u'\u4e2d\u6587')

    def test_logs(self):
        # assertLogs()- Tests that Python has logged at least one message on the logger or a child of the logger;
        # ensures this is with at least the level we mention.
        with self.assertLogs(level='INFO') as log:
            logging.info('Log message')
            self.assertEqual(len(log.output), 1)
            self.assertEqual(len(log.records), 1)
            self.assertIn('Log message', log.output[0])
        
    def test_warns(self):	
        # assertWarns()- Tests that Python triggers a warning when we call the callable with positional/
        # \ keyword arguments we also passed to this method.
        self.assertWarns(Warning,isZero,0)
                    #  or
        #     with self.assertWarns(UserWarning):
        #         warnings.warn('Some warning')

    def test_warns_regex(self):
        # assertWarnsRegex()- Tests that regex matches on the message for the triggered warning;
        #  similar to assertWarns().
        with self.assertWarnsRegex(DeprecationWarning, "^deprecate[a-z]$"):
            warnings.warn("deprecated", DeprecationWarning)

# Define a main function on here.
if __name__ == "__main__":
    unittest.main()