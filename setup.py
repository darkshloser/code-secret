import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="code-secret-DARKSHLOSER",
    version="0.0.1",
    author="Dobromir Kovachev",
    author_email="dobromir.mail@gmail.com",
    description="Tool for securing sensitive code private/public repositories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/code-secret",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
