from . import bbox

class Chunk:
    def __init__(self, volume, mip, coord):
        self._mip = mip
        self._coord = coord
        self._volume = volume

    def coordinate(self):
        return self._coord

    def mip_level(self):
        return self._mip

    def primary_child_coord(self):
        return [x*2 for x in self._coord]

    def chunk_bbox(self):
        mip_chunk_dim = [int(2**self._mip*x) for x in self._volume.chunk_dim()]
        chunk_offset = [offset + x*dim for offset,x,dim in zip(self._volume.offset(), self._coord, mip_chunk_dim)]
        chunk_end = [x+y for x,y in zip(chunk_offset, mip_chunk_dim)]
        return chunk_offset+chunk_end

    def data_bbox(self):
        return bbox.intersection(self.chunk_bbox(), self._volume.data_bbox())

    def has_data(self):
        chunk_bbox = self.chunk_bbox()
        if bbox.overlap(chunk_bbox, self._volume.data_bbox()):
            return True
        return False

    def print_chunk_info(self):
        print("mip level: ", self._mip, ", coord: ", self._coord, ", bbox: ", self.data_bbox(), ", boundary: ", self.boundary_flags())

    def possible_children(self):
        c = []

        x, y, z= self.primary_child_coord()

        c = {"_".join([str(i),str(j),str(k)]): Chunk(self._volume, self._mip-1, [x+i,y+j,z+k]) for i in range(2) for j in range(2) for k in range(2)}

        return c

    def possible_neighbours(self):
        c = []

        x, y, z= self._coord

        c = {"_".join([str(i),str(j),str(k)]): Chunk(self._volume, self._mip, [x+i,y+j,z+k]) for i in range(-1,2,1) for j in range(-1,2,1) for k in range(-1,2,1)}

        return c

    def children(self):
        if self._mip == 0:
            return []

        if not self.has_data():
            print("empty chunk")
            return []

        return [i for i in self.possible_children().values() if i.has_data()]

    def neighbours(self):
        if self._mip == self._volume.top_mip_level():
            return []

        if not self.has_data():
            print("empty chunk")
            return []

        return [i for i in self.possible_neighbours().values() if i.has_data()]

    def boundary_flags(self):
        flags = [0,0,0,0,0,0]
        data_dimInChunks = self._volume.mip_level_data_dim_in_chunks(self._mip)

        for i in range(3):
            if self._coord[i] == 0:
                flags[i] = 1

            if self._coord[i] == data_dimInChunks[i] - 1:
                flags[i+3] = 1

        return flags
