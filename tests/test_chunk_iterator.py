from chunk_iterator import ChunkIterator

#v = ChunkIterator([10240, 7680, 0, 65015, 43715, 1002], [1024, 1024, 1024])
v = ChunkIterator([0,0,0,2048,2048,256], [500, 500, 100])
print v.offset()
print v.data_dim()
print v.data_bbox()
print v.top_mip_level()
print v.mip_level_data_dim_in_chunks(4)
print v.mip_level_data_dim_in_chunks(5)

for c in v:
    c.print_chunk_info()
