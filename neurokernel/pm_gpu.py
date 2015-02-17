#!/usr/bin/env python

"""
Port mapper for GPU memory.
"""

import numbers

import numpy as np
import pycuda.gpuarray as gpuarray
import pycuda.elementwise as elementwise
import pycuda.tools as tools

from plsel import PortMapper

class GPUPortMapper(PortMapper):
    """
    Maps a PyCUDA GPUArray to/from path-like port identifiers.
    """

    def __init__(self, selector, data=None, portmap=None, make_copy=True):
        super(PortMapper, self).__init__(selector, portmap)
        N = len(self)

        if data is None or len(data) == 0:
            self.data = gpuarray.empty(0, np.double)
        else:
            # Can only handle 1D data arrays:
            assert np.ndim(data) == 1

            # The integers in the port map must be valid indices into the
            # data array:
            assert max(self.portmap) < len(data)

            # The port mapper may map identifiers to some portion of the data array:
            assert N <= len(data)

            if isinstance(data, gpuarray.GPUArray):
                if make_copy:
                    self.data = data.copy()
                else:
                    self.data = data
            else:

                # If the initial data array isn't already on the GPU, it must be
                # copied:
                self.data = gpuarray.to_gpu(data)

        self.data_ctype = tools.dtype_to_ctype(self.data.dtype)

    def get_inds_nonzero(self):
        raise NotImplementedError

    def get_ports_nonzero(self):
        raise NotImplementedError

    def set(self, selector, data):
        raise NotImplementedError

    def get(self, selector):
        raise NotImplementedError

    __getitem__ = get
    __setitem__ = set

    def get_by_inds(self, inds):
        """
        Retrieve mapped data specified by integer index.
        
        Parameters
        ----------
        inds : sequence of int
            Integer indices of data elements to return.
        
        Returns
        -------
        result : numpy.ndarray
            Selected data.
        """

        assert len(np.shape(inds)) == 1
        assert issubclass(inds.dtype.type, numbers.Integral)

        N = len(inds)
        assert N <= len(self.data)
        inds_ctype = tools.dtype_to_ctype(inds.dtype)
        if not isinstance(inds, gpuarray.GPUArray):
            inds = gpuarray.to_gpu(inds)
        v = "{data_ctype} *dest, {inds_ctype} *inds, {data_ctype} *src".format(data_ctype=self.data_ctype, inds_ctype=inds_ctype)
        result = gpuarray.empty(N, dtype=self.data.dtype)

        func = elementwise.ElementwiseKernel(v, "dest[i] = src[inds[i]]")
        func(result, inds, self.data, range=slice(0, N, 1))
        return result.get()

    def set_by_inds(self, inds, data):
        """
        Set mapped data by integer indices.

        Parameters
        ----------
        inds : sequence of int
            Integer indices of data elements to update.
        data : numpy.ndarray
            Data to assign.
        """

        assert len(np.shape(inds)) == 1
        assert self.data.dtype == data.dtype
        assert issubclass(inds.dtype.type, numbers.Integral)

        N = len(inds)
        assert N == len(data)
        inds_ctype = tools.dtype_to_ctype(inds.dtype)
        if not isinstance(inds, gpuarray.GPUArray):
            inds = gpuarray.to_gpu(inds)
        if not isinstance(data, gpuarray.GPUArray):
            data = gpuarray.to_gpu(data)
        v = "{data_ctype} *dest, {inds_ctype} *inds, {data_ctype} *src".format(data_ctype=self.data_ctype, inds_ctype=inds_ctype)
        
        func = elementwise.ElementwiseKernel(v, "dest[inds[i]] = src[i]")
        func(self.data, inds, data, range=slice(0, N, 1))

