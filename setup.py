import platform
from setuptools import setup
from setuptools import find_packages
from setuptools import Extension


extra_compile_args = [
    '-std=c++11',
    '-O3',
    '-Wall',
    '-Wextra',
    '-Wconversion',
    '-fno-strict-aliasing',
    '-fno-rtti',
]
extra_link_args = []

if platform.system() == 'Darwin':
    extra_compile_args += ['-mmacosx-version-min=10.9']
    extra_link_args = ["-stdlib=libc++", "-mmacosx-version-min=10.9"]


setup(
    name="python-rocksdb",
    version='0.6.9',
    description="Python bindings for RocksDB",
    keywords='rocksdb',
    author='Ming Hsuan Tu',
    author_email="qrnnis2623891@gmail.com",
    url="https://github.com/twmht/python-rocksdb",
    license='BSD License',
    setup_requires=['setuptools>=25', 'Cython>=0.20'],
    install_requires=['setuptools>=25'],
    package_dir={'rocksdb': 'rocksdb'},
    packages=find_packages('.'),
    ext_modules=[Extension(
        'rocksdb._rocksdb',
        ['rocksdb/_rocksdb.pyx'],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
        language='c++',
        libraries=['rocksdb', 'snappy', 'bz2', 'z', 'lz4'],
    )],
    extras_require={
        "doc": ['sphinx_rtd_theme', 'sphinx'],
        "test": ['pytest'],
    },
    include_package_data=True
)
