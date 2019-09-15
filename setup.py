import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loggerpy",
    version="0.0.8",
    author="Mattia Sanchioni",
    author_email="mattia.sanchioni.dev@gmail.com",
    description="A simple logger for everyday tasks",
    keywords="logger log logging simple pylogger py-logger loggerpy logger-py simplelogger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mett96/loggerpy",
    packages=setuptools.find_packages(),
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)