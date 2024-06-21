from setuptools import setup
from torch.utils import cpp_extension

setup(
    name='knn',
    ext_modules=[
        cpp_extension.CUDAExtension('knn', ['simpleknn.cu'])
    ],
    cmdclass={'build_ext': cpp_extension.BuildExtension}
)

