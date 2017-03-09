#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from mydict import Dict

class TestDict(unittest.TestCase):

    def test__init(self,**kw):
        d = Dict(a = 1,b = 'test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,Dict))

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')

    def test_keyarror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
		
    def test_attrarror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
	
    def setUp(self):
        print('method is running..')
        #d = Dict()
		
    def tearDown(self):
        print('method is over..')
		
		
if __name__ == '__main__':
    unittest.main()
