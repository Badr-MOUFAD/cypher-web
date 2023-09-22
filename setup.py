from setuptools import setup

setup(
    name="cypherweb",
    version="0.1.0",
    description="Query any web page with Cypher",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Anas AIT AOMAR",
    author_email="anas1999@gmail.com",
    packages=["cypherweb"],
    install_requires=[
        # List any dependencies your module requires
        "lark",
        "networkx",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
