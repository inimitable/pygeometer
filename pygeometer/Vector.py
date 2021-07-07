#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Vectors, including special case 3D and 2D vectors."""

from math import acos

from pygeometer.Pointlike import _PointlikeND
from pygeometer.type_helpers import Number


class VectorND(_PointlikeND):

    @property
    def magnitude(self):
        return sum(map(lambda x: x ** 2, self.coords)) ** 0.5

    def scalar(self, other: Number):
        """Computes the scalar multiple of this vector."""
        cls = self.__class__
        return cls([x * other for x in self.coords])

    def dot(self, other: 'VectorND'):
        """Computes the dot product of two vectors."""
        assert self.dimension == other.dimension
        return sum(self[x] * other[x] for x in range(self.dimension))

    def angle(self, other: 'VectorND'):
        """Computes the angle between two vectors."""
        if self.magnitude == 0 or other.magnitude == 0:
            raise ValueError('cannot find angle between null vector and anything else')
        return acos(((self.dot(other)) / self.magnitude) / other.magnitude)

    def __mul__(self, other: Number):
        return self.scalar(other)


class Vector3D(VectorND):

    def cross(self, other: 'Vector3D'):
        """Computes the cross product of two vectors."""
        return Vector3D(
            (
                self[1] * other[2] - other[1] * self[2],
                self[2] * other[0] - other[2] * self[0],
                self[0] * other[1] - other[0] * self[1]
            )
        )
