from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py
import os
import shutil

class CustomBuild(_build_py):
    def run(self):
        # Ensure the .so file is included in the package directory
        if not os.path.exists('fbxpythonbindings'):
            os.makedirs('fbxpythonbindings')
        
        # Copy the .so file to the package directory
        shutil.copy('fbx.cpython-312-x86_64-linux-gnu.so', 'fbxpythonbindings/')
        
        # Also copy the FbxCommon.py file
        shutil.copy('FbxCommon.py', 'fbxpythonbindings/')
        
        super().run()

setup(
    name='fbxpythonbindings',
    version='1.0.0',
    description='FBX Python Bindings',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    package_data={'fbxpythonbindings': ['*.so', 'FbxCommon.py']},
    include_package_data=True,
    cmdclass={'build_py': CustomBuild},
    zip_safe=False,
)
