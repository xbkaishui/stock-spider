from distutils.core import setup
import setuptools

setup(
    name='stock-spider',
    version='1.3.0',
    packages=['stock-spider'],
    package_dir={'spider': 'doc'},
    package_data={'spider': ['exchanges/*.csv']},
    include_package_data=True,
    author='xbkaishui',
    author_email='xbkaishui@126.com',
    description='Spider US Stock',
    long_description=open('README.md').read(),
    url='http://xbkaishui.github.io/',
    download_url='http://pypi.python.org/pypi/stock-spider',
    keywords='Spider US Stock'.split(),
    license='Apache License 2.0',
    install_requires=[
        "beautifulsoup4 >= 4.2.1"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Investment',
    ]
)
