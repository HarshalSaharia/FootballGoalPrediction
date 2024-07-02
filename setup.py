from setuptools import setup, find_packages

setup(
    name='football_project',
    version='0.1.0',
    author='HarshalSaharia',
    author_email='harshalsanjaysaharia@gmail.com',
    description='A project for predicting football player performance metrics.',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'flask',
        'pymongo',
        'gunicorn',
        'dvc'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
