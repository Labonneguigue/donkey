from donkeycar.parts.transform import Lambda, Cropper
import unittest
import pytest
import numpy as np

class TestTransform(unittest.TestCase):

    def f(self,a):
        return a + 1

    def f2(self,a, b):
        return a + b + 1

    def test_lambda_one_arg(self):
        l = Lambda(self.f)
        b = l.run(1)
        assert b == 2

    def test_lambda_two_args(self):
        l = Lambda(self.f2)
        b = l.run(1, 1)
        assert b == 3

    def test_cropper(self):
        a = np.array([[1,2,3],[4,5,6],[7,8,9]])
        b = Cropper.crop(a)
        assert( a.all() == b.all() )

        d = Cropper.crop(a, (1,1), (0,0))
        d_true = np.array([[4, 5, 6]])
        assert(d.all() == d_true.all())

        e = Cropper.crop(a, (0,0), (1,1))
        e_true = np.array([[2],[5],[8]])
        assert(e.all() == e_true.all())
        
        c = Cropper(0,0,1,1)
        E = c.run(a)
        assert(E.all() == e_true.all())
