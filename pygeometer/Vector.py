#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""docstring"""
from math import acos

from pygeometer.Pointlike import _PointlikeND
from pygeometer.type_helpers import Number


class VectorND(_PointlikeND):
    _cname = 'VectorND'

    @property
    def magnitude(self):
        return sum(map(lambda x: x ** 2, self.coords)) ** 0.5

    def __mul__(self, other: Number):
        return self.scalar(other)

    def scalar(self, other: Number):
        """Computes the scalar multiple of this vector."""
        cls = self.__class__
        return cls([x * other for x in self.coords])

    def dot(self, other: 'VectorND'):
        """Computes the dot product of two vectors."""
        assert self.dimension == other.dimension
        return sum(self[x] * other[x] for x in range(self.dimension))




class Vector3D(VectorND):
    _cname = 'Vector3D'

    def cross(self, other: 'Vector3D'):
        """Computes the cross product of two vectors."""
        return Vector3D(
            (
                self[1] * other[2] - other[1] * self[2],
                self[2] * other[0] - other[2] * self[0],
                self[0] * other[1] - other[0] * self[1]
            )
        )

    def angle(self, other: 'Vector3D'):
        """Computes the angle between two vectors."""
        return acos(((self.dot(other)) / self.magnitude) / other.magnitude)
