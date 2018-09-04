#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Common behaviors for Points and Vectors."""

class _PointlikeND:

    _cname = '_PointlikeND'

    def __init__(self, dims):
        self.dimension = len(dims)
        self.coords = tuple(dims)
        self._dimdict = dict()

        for idx, _dim in enumerate(dims):
            self._dimdict[idx] = _dim

    def __getdim(self, idx):
        return self._dimdict.get(idx, 0)

    def __eq__(self, other):
        return self.coords == other.coords

    def __samedim(self, other):
        """True if self and other have the same dimensionality."""
        if self.dimension == other.dimension:
            return True

    def __add__(self, other):
        """Sums two pointlikes (as if they were vectors.)"""
        dim_range = range(max(self.dimension, other.dimension))
        cls = self.__class__
        return cls(tuple([self[x] + other[x] for x in dim_range]))

    def __sub__(self, other):
        """Subtracts one pointlike from another (as if they were vectors.)"""
        dim_range = range(max(self.dimension, other.dimension))
        cls = self.__class__
        return cls(tuple([self[x] - other[x] for x in dim_range]))

    def __getitem__(self, item):
        if isinstance(item, str) and item in 'xyz':
            item = 'xyz'.index(item)
        return self.__getdim(item)

    def distance(self, other):
        return sum(map(lambda x: x ** 2, (self - other).coords)) ** 0.5

    def __repr__(self):
        #cls = str(self.__class__).split('.')[-1][:-2]
        return f"{self._cname}({self.coords})"

