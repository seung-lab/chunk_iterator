from __future__ import division
import math
from chunk import Chunk

class ChunkIterator:
    def __init__(self, volume_bbox, chunk_dim):
        self._offset = volume_bbox[0:3]
        self._chunk_dim = chunk_dim
        self._data_dim = [volume_bbox[i+3]-volume_bbox[i] for i in range(3)]
        dim_in_chunks = self.mip_level_data_dim_in_chunks(0)
        self._top_mip_level = int(math.ceil(math.log(max(dim_in_chunks))/math.log(2)))
        self._chunks = [Chunk(self, self._top_mip_level, [0,0,0])]

    def offset(self):
        return self._offset

    def chunk_dim(self):
        return self._chunk_dim

    def data_dim(self):
        return self._data_dim

    def top_mip_level(self):
        return self._top_mip_level

    def mip_level_data_dim(self, level):
        return [int((x - 1) / 2**level + 1) for x in self.data_dim()];

    def mip_level_data_dim_in_chunks(self, level):
        return [int(math.ceil(x/y)) for x,y in zip(self.mip_level_data_dim(level), self._chunk_dim)]

    def data_bbox(self):
        data_end = [x+y for x, y in zip(self._offset, self._data_dim)]
        return self._offset + data_end

    def __iter__(self):
        return self

    def next(self):
        if len(self._chunks) == 0:
            raise StopIteration
        c = self._chunks.pop(0)
        self._chunks += c.children()
        return c
