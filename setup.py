from setuptools import setup, find_packages
from glob import glob

setup(
    name='fbxpythonbindings',
    version='1.0.0',
    description='FBX Python Bindings',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    package_data={
        '': ['FbxCommon.py', '*.so'],  # Ensure .so and FbxCommon.py are included
    },
    include_package_data=True,
    zip_safe=False,
)
