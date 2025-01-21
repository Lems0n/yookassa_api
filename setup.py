from setuptools import setup, find_packages


from setuptools import setup, find_packages

setup(
    name='yookassa_api',
    version='0.1.0',
    author='Lemson',
    author_email='abdulla.dev@mail.ru',
    description='Python package for YooKassa API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Lems0n/yookassa_api',  
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',  
    install_requires=[
        'pydantic',
        'requests',
        'aiohttp',
    ],
)

    