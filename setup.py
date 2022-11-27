from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(
    name='worldcup',
    version="0.0.0",
    description="World cup prediction",
    license="MIT",
    author="Alec Sharp",
    author_email="alecsharpie@gmail.com",
    url="https://github.com/alecsharpie/worldcup_2022",
    install_requires=requirements,
    packages=find_packages(),
    test_suite="tests",
    # include_package_data: to install data from MANIFEST.in
    include_package_data=True,
    zip_safe=False)
