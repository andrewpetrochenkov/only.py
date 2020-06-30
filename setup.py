import setuptools

setuptools.setup(
    name='only',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
