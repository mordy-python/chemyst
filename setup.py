from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='chemyst',
    version='2.2.1',
    description='Useful functions to work with basic chemistry and stochiemetry',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Mordy Waldo',
    author_email='imky171@gmail.com',
    keywords=['Chemistry', 'Chem', 'Periodic table'],
    url='https://github.com/mordy-python/chemyst',
    download_url='https://pypi.org/project/chemyst/'
)

install_requires = []

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)