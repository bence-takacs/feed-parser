from setuptools import setup

setup(
    name='fp',
    version='0.9.2',
    scripts=['__init__.py'],
    url='https://github.com/pypa/sampleproject',
    author='Bence Takács',
    author_email='takacs.bence@gmail.com',
    install_requires=[
        'requests', 'beautifulsoup4', 'logging'
    ]
)
