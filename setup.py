from setuptools import setup

setup(
    name='feed_parser',
    version='0.9.4',
    scripts=['feed_parser/__init__.py', 'feed_parser/FeedParser.py'],
    url='https://github.com/bence-takacs/feed-parser',
    author='Bence Takacs',
    author_email='takacs.bence@gmail.com',
    install_requires=[
        'requests', 'beautifulsoup4', 'logging', 'web.py'
    ]
)
