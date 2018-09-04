#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Test suite for Point* objects."""
from pygeometer.Point import PointND
from unittest import TestCase
from random import randint
from functools import partial


class TestPointND(TestCase):

    def test_distance(self):
        a = PointND([5, 5, 0])
        b = PointND([1, 1, 2])
        self.assertEqual(a.distance(b), 6.0)

    def test_commutative(self):
        f = partial(randint, 0, 100)
        for x in range(10):
            a = PointND([f(), f(), f(), f()])
            b = PointND([f(), f(), f(), f()])
            self.assertEqual(a.distance(b), b.distance(a))

    def test_diff_dim_distance(self):
        a = PointND([4, 5, 5])
        b = PointND([1, 1])
        self.assertEqual(b.distance(a), 7.0710678118654755)

    def test_commutative_add(self):
        a = PointND([1, 2, 2])
        b = PointND([2, 1, 4])
        self.assertEqual(a + b, b + a)

    def test_identity(self):
        f = partial(randint, 0, 100)
        for x in range(10):
            a = PointND([f(), f(), f(), f()])
            self.assertEqual(PointND([0, 0, 0]) + a, a)

    def test_repr(self):
        a = PointND([1, 5, 4, 5])
        self.assertEqual(a.__repr__(), 'PointND((1, 5, 4, 5))')

    def test_nearest(self):
        a = PointND((0, 0, 0, 0, 0))
        b = PointND((1, 2, 4, 5, 6))
        c = PointND((3, 0, 0, 0, 0))
        d = PointND((1, 4, 2, 4, 1))
        others = (b, c, d)

        self.assertEqual(a.nearest(others), c)
        self.assertEqual(a.nearest_n(others, 2), [c, d])
