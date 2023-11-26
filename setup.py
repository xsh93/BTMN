from setuptools import setup

setup(
    name='btmn',
    version='1.0',
    description='Bidirectional Time-series Mechanistic Network (BTMN)',
    author='',
    author_email='',
    packages=["btmn"],
    install_requires=[
        'torch==2.0.0',
        'numpy>=1.23.5',
        'pandas>=1.5.2',
    ]
)
