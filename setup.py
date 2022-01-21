import setuptools
from setuptools import setup
import io

with io.open('README.md', 'rt', encoding='utf8') as f:
    long_description = f.read()

setup(
    name='feishu_chatbot',
    version="0.0.3",
    install_requires=['voluptuous>=0.12.2', 'requests>=2.25.0'],
    url='https://github.com/rexyan/feishu_chatbot',
    license='MIT',
    author='RexYan',
    author_email='rex_yan@126.com',
    description='feishu chatbot api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    platforms=['all'],
    include_package_data=True,
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