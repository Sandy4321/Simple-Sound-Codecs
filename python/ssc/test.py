#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import array
from math import sin, pi

import dm
from aux import max_int, min_int, WIDTH_TYPE

MAX_8 = max_int(1)
MAX_16 = max_int(2)
MAX_32 = max_int(4)

MIN_8 = max_int(1)
MIN_16 = min_int(2)
MIN_32 = min_int(4)

# Defines Sample frecuency/bitrate and test_data subsections 
TEST_FS = 44100
TEST_T = 0.5

'''
        # test_t seconds of 440 hz sinouidal sound at 0.9 amplitude
        freq = 440.0 * 2 * pi / TEST_FS
        for i in range(samples):
            f = 0.9 * sin(freq * i)
            raw8.append(int(MAX_8 * f))
            raw16.append(int(MAX_16 * f))
            raw32.append(int(MAX_32 * f))
'''

class ToLin2dmBadInput(unittest.TestCase):


    def setUp(self):
        '''Fills test data'''
        raw8 = array.array(WIDTH_TYPE[1])
        raw16 = array.array(WIDTH_TYPE[2])
        raw32 = array.array(WIDTH_TYPE[4])
        samples = int(TEST_T // TEST_FS)

        # test_t seconds of pure silence
        for i in range(samples):
            raw8.append(0)
            raw16.append(0)
            raw32.append(0)

        self.test_data8 = raw8.tostring()
        self.test_data16 = raw16.tostring()
        self.test_data32 = raw32.tostring()


    def test_missing_input(self):
        '''lin2dem should fail with missing fragment data'''
        self.assertRaises(Exception, dm.lin2dm, None, 1)


    def test_invalid_width(self):
        '''lin2dm should fail with invalid width'''
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, 0)
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, -1)
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, 40)
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, '4')
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, None)
        

    def test_invalid_a(self):
        '''lin2dm should fail with invalid A value'''
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, 1, a_cte=-0.5)
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, 1, a_cte=1.5)
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, 1, a_cte=0)
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, 1, a_cte=-2)
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, 1, a_cte='0.5')
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, 1, a_cte=None)


    def test_invalid_deta(self):
        '''lin2dm should fail with invalid Delta value'''
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, 1, delta=0)
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, 1, delta=-1)
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, 1, delta='32')
        self.assertRaises(Exception, dm.lin2dm, self.test_data8, 1, delta=MAX_8)
        self.assertRaises(Exception, dm.lin2dm, self.test_data16, 2, delta=MAX_16)
        self.assertRaises(Exception, dm.lin2dm, self.test_data32, 4, delta=MAX_32)


# MAIN
if __name__ == '__main__':
    unittest.main()

