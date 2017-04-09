from setuptools import setup

setup(
    name='feed-parser',
    version='0.9.1',
    scripts=['fp.py'],
    install_requires=[
        'requests', 'beautifulsoup4', 'logging'
    ]
)