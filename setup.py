from setuptools import setup, find_packages

setup(
    name='Cope',
    version='1.1.0',
    description='A bunch of generic functions and classes useful in multiple projects',
    url='https://github.com/smartycope/Cope',
    author='Copeland Carter',
    author_email='smartycope@gmail.com',
    license='GPL 3.0',
    # packages=['Cope'],
    packages=find_packages(),
    install_requires=[],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.9',
    ],
)
