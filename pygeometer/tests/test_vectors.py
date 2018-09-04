#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""docstring"""
from math import pi
from unittest import TestCase
from pygeometer.Point import PointND
from pygeometer.Vector import Vector3D, VectorND


class TestVectorND(TestCase):
    a = VectorND([1, 2, 2])
    b = VectorND([2, 1, 4])

    def test_dot(self):
        a = self.a
        b = self.b
        self.assertEqual(a.dot(b), 12)

    def test_mag(self):
        b = self.b
        self.assertEqual(b.magnitude, 21 ** 0.5)

    def test_angle(self):
        a = VectorND([0, 0, 0, 1])
        b = VectorND([0, 1, 0, 0])
        self.assertAlmostEqual(a.angle(b), pi / 2, places=10)
        self.assertEqual(a.angle(b), b.angle(a))

    def test_null_rejected(self):
        a = VectorND([0, 0])
        b = VectorND([1, 0])
        with self.assertRaises(ValueError):
            a.angle(b)

    def test_repr(self):
        a = self.a
        self.assertEqual(a.__repr__(), 'VectorND((1, 2, 2))')


class TestVector3D(TestCase):
    a = Vector3D([1, 2, 2])
    b = Vector3D([2, 1, 4])

    def test_cross(self):
        a = self.a
        b = self.b
        self.assertEqual(a.cross(b).coords, (6, 0, -3))

    def test_cross_anticommutative(self):
        a = self.a
        b = self.b
        self.assertEqual(a.cross(b), (b.cross(a)) * -1)

    def test_from_points(self):
        a = PointND([1, 1, 1, 1, 1])
        b = PointND([2, 2, 2, 2, 5])
        self.assertEqual(a.vector_to(b), VectorND([1, 1, 1, 1, 4]))

    def test_repr(self):
        a = self.a
        self.assertEqual(a.__repr__(), 'Vector3D((1, 2, 2))')
