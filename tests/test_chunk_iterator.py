from chunk_iterator import ChunkIterator

v = ChunkIterator([10240, 7680, 0, 65015, 43715, 1002], [1024, 1024, 1024])
print v.offset()
print v.dataDim()
print v.dataBBox()
print v.topMipLevel()
print v.mipLevelDataDimInChunks(4)
print v.mipLevelDataDimInChunks(5)

for c in v:
    c.print_chunk_info()
