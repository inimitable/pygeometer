#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Provides 2D, 3D and nD point objects."""
from typing import Sequence

from pygeometer.Vector import VectorND
from pygeometer.Pointlike import _PointlikeND
from pygeometer.type_helpers import Number


class PointND(_PointlikeND):
    _cname = 'PointND'

    def vector_to(self, other: 'PointND') -> 'VectorND':
        return VectorND((other - self).coords)

    def furthest(self, points: Sequence['PointND']) -> 'PointND':
        """Return the furthest point from this point."""
        return self.furthest_n(points, 1)[0]

    def furthest_n(self, points: Sequence['PointND'], n: int) -> Sequence['PointND']:
        """Return the furthest n points from this point."""
        return sorted(points, key=lambda x: self.distance(x), reverse=True)[:n]

    def nearest(self, points: Sequence['PointND']) -> 'PointND':
        """Return the closest point to this point."""
        return self.nearest_n(points, 1)[0]

    def nearest_n(self, points: Sequence['PointND'], n: int) -> Sequence['PointND']:
        """Return the closest n points to this point."""
        point_count = len(points)
        n = min(n, point_count)

        return sorted(points, key=lambda x: self.distance(x))[:n]


class Point2D(PointND):

    def __init__(self, dims: Sequence[Number]):
        super(Point2D, self).__init__(dims)
        self.x = dims[0]
        self.y = dims[1]


class Point3D(PointND):

    def __init__(self, dims: Sequence[Number]):
        super(Point3D, self).__init__(dims)
        self.x = dims[0]
        self.y = dims[1]
        self.z = dims[2]
