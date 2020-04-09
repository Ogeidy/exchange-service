from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="exchange-service",
    version="0.1",
    author="Yakov Mamontov",
    author_email="yakov-mamontov@yandex.ru",
    description="Web service for storing JSON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ogeidy/exchange-service",
    packages=find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
