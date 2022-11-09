import setuptools

setuptools.setup(
    name="chunk-iterator", # Replace with your own username
    version="0.0.2",
    author="Ran Lu",
    author_email="ranl@princeton.edu",
    description="Recursively dividing input bbox into chunks as an octree",
    url="https://github.com/seung-lab/chunk_iterator",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
