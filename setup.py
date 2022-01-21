import setuptools
from setuptools import setup
import io
import re

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('chatbot/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='feishu_chatbot',
    version="1.0.0",
    install_requires=['voluptuous'],

    url='https://github.com/rexyan/feishu_chatbot',
    license='MIT',
    author='Rex Yan',
    author_email='rex_yan@126.com',
    description='feishu chatbot api',
    long_description=readme,
    packages=setuptools.find_packages(),
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]

)