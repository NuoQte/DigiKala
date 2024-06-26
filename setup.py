from setuptools import setup, find_packages

setup(
    name='DigiKala',
    version='1.0',
    packages=find_packages(),
    license='MIT',
    description='DigiKala library to connect and work with digikala.com!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='NuoQTe',
    author_email='nuoqte@gmail.com',
    url='https://github.com/NuoQte/DigiKala',
    install_requires=['aiohttp']
)