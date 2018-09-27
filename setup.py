from setuptools import setup, find_packages

install_requires = [
        "Scrapy>=1.3.0",
        "Flask>=0.10.1",
        "Twisted>=15.4.0",
        "six>=1.10.0"
]

setup(
    name='ArachneScrapy',
    version='0.6.1',
    author='Nonpawit Teerachetmongkol',
    author_email='nonpawit.tee@gmail.com',
    packages=find_packages(),
    test_suite='arachne.tests',
    url='https://github.com/n3n/arachne',
    license='BSD',
    description='API for Scrapy spiders',
    long_description=open('README.rst').read(),
    install_requires=install_requires,
)
