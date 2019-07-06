import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="novncbot",
    version="0.0.1",
    author="Shawn Johnson",
    author_email="sjohnson@axiomega.com",
    description="An asynchronous noVNC client",
    long_description=long_description,
    url="https://github.com/shawrkbait/novncbot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)