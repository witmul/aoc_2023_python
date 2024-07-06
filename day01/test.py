import unittest
from part01 import get_number_pair as get_number_pair_01
from part02 import get_number_pair as get_number_pair_02

class TestSolutionPart1Function(unittest.TestCase):
    def test_01(self):
        self.assertEqual(get_number_pair_01('eighthree7ssrrsninefourfour'), 77)
    def test_02(self):
        self.assertEqual(get_number_pair_01('onefour5ghthreezero8sevenm'), 58)
    def test_03(self):        
        self.assertEqual(get_number_pair_01('1lv'), 11)
    def test_04(self):        
        self.assertEqual(get_number_pair_01('z57sevenxpfgntjnphcntj3bv'), 53)
    def test_05(self):        
        self.assertEqual(get_number_pair_01('dxzsnnsnj1mkctsix4qqbxscdfm9xvngln'), 19)                    
    def test_06(self):        
        self.assertEqual(get_number_pair_01('ndeightwosnlvkv8jdllrtwo741'), 81)          
    def test_07(self):        
        self.assertEqual(get_number_pair_01('6f'), 66)
    def test_08(self):        
        self.assertEqual(get_number_pair_01('fivesseven47lndonesevenvfdvkp'), 47)     
    def test_09(self):        
        self.assertEqual(get_number_pair_01('6sevenmdvsdqxt3vnzdgninejkdjmzngckfcdh9'), 69)          
    def test_10(self):        
        self.assertEqual(get_number_pair_01('nkkxzlrkgfonesevenfour7twompjpqdsvpp'),77)
    def test_11(self):        
        self.assertEqual(get_number_pair_01('337'),37)
    def test_12(self):        
        self.assertEqual(get_number_pair_01('7eight7'),77)
    def test_13(self):        
        self.assertEqual(get_number_pair_01('3stuffthree'),33)
    def test_14(self):        
        self.assertEqual(get_number_pair_01('9sixqnine9jk9six'),99)
    def test_15(self):        
        self.assertEqual(get_number_pair_01('fplzzhthreethree7sqnsmrljgsmnpktfkhzdpqfkone'),77)
    def test_16(self):        
        self.assertEqual(get_number_pair_01('vneightwonine7ntgxbzfouronetwofzzgkkhtx3nine'),73)        
    def test_17(self):        
        self.assertEqual(get_number_pair_01('six26'),26)          
    def test_18(self):        
        self.assertEqual(get_number_pair_01('seven2931nhxpkppdv445'),25)        
    def test_19(self):        
        self.assertEqual(get_number_pair_01('6oneighthlf'),66)        
    def test_20(self):        
        self.assertEqual(get_number_pair_01('nrzpqk3fivesldclpcbfmdtbbhpxonethreeeightwor'),33)    

class TestSolutionPart2Function(unittest.TestCase):
    def test_01(self):
        self.assertEqual(get_number_pair_02('eighthree7ssrrsninefourfour'), 84)
    def test_02(self):
        self.assertEqual(get_number_pair_02('onefour5ghthreezero8sevenm'), 17)
    def test_03(self):        
        self.assertEqual(get_number_pair_02('1lv'), 11)
    def test_04(self):        
        self.assertEqual(get_number_pair_02('z57sevenxpfgntjnphcntj3bv'), 53)
    def test_05(self):        
        self.assertEqual(get_number_pair_02('dxzsnnsnj1mkctsix4qqbxscdfm9xvngln'), 19)                    
    def test_06(self):        
        self.assertEqual(get_number_pair_02('ndeightwosnlvkv8jdllrtwo741'), 81)          
    def test_07(self):        
        self.assertEqual(get_number_pair_02('6f'), 66)
    def test_08(self):        
        self.assertEqual(get_number_pair_02('fivesseven47lndonesevenvfdvkp'), 57)     
    def test_09(self):
        self.assertEqual(get_number_pair_02('6sevenmdvsdqxt3vnzdgninejkdjmzngckfcdh9'), 69)          
    def test_10(self):        
        self.assertEqual(get_number_pair_02('nkkxzlrkgfonesevenfour7twompjpqdsvpp'),12)
    def test_11(self):        
        self.assertEqual(get_number_pair_02('337'),37)
    def test_12(self):        
        self.assertEqual(get_number_pair_02('7eight7'),77)
    def test_13(self):        
        self.assertEqual(get_number_pair_02('3stuffthree'),33)
    def test_14(self):        
        self.assertEqual(get_number_pair_02('9sixqnine9jk9six'),96)
    def test_15(self):        
        self.assertEqual(get_number_pair_02('fplzzhthreethree7sqnsmrljgsmnpktfkhzdpqfkone'),31)
    def test_16(self):        
        self.assertEqual(get_number_pair_02('vneightwonine7ntgxbzfouronetwofzzgkkhtx3nine'),89)        
    def test_17(self):        
        self.assertEqual(get_number_pair_02('six26'),66)          
    def test_18(self):        
        self.assertEqual(get_number_pair_02('seven2931nhxpkppdv445'),75)        
    def test_19(self):        
        self.assertEqual(get_number_pair_02('6oneighthlf'),68)        
    def test_20(self):        
        self.assertEqual(get_number_pair_02('nrzpqk3fivesldclpcbfmdtbbhpxonethreeeightwor'),32)    
        
