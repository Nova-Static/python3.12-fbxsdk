from setuptools import setup, find_packages

setup(
    name='fbxpythonbindings',
    version='1.0.0',
    description='FBX Python Bindings',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    package_data={
        '': ['fbx.cpython-312-x86_64-linux-gnu.so', 'FbxCommon.py'],
    },
    include_package_data=True,
    zip_safe=False,
)
