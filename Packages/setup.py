from setuptools import setup, find_packages

setup(
    name= 'cleaning',
    version= '0.4',
    packages= find_packages(exclude=['Tests*']),
    license= 'None',
    description= 'Cleaning package for dataframes',
    long_description= open('README.md').read(),
    install_requires= ['pandas', 'numpy'],
    author= 'Kyle',
    author_email= 'kgerrarde96@gmail.com'
)