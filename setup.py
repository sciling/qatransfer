from setuptools import setup, find_packages

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='qatransfer',
    url='git@github.com:sciling/qatransfer.git',
    author='VB',
    author_email='',
    # Needed to actually package something
    # packages=['basic'],
    packages=find_packages(),
    # Needed for dependencies
    install_requires=['numpy', 'nltk', 'xmltodict'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Creating a package for container',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
