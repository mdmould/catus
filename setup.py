from setuptools import setup, find_packages

name = 'catus'
version = '0.0.6'

with open('README.md' ,'r') as f:
    long_description = f.read().strip()

setup(
    name=name,
    version=version,
    description=name,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/mdmould/{name}',
    author='Matthew Mould',
    author_email='mattdmould@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'kaydee',
        ],
    python_requires='>=3.7',
    )
