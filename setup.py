import setuptools

with open("README.md","r",encoding="utf-8")as f:
    long_distribution= f.read()
__version__="0.0.0"
repo_name="Annimated-picture-GAN"
author="bhavithakotni"
author_email="kotnibhavitha1995@gmail.com"
src_name="animated-picture"

setuptools.setup(
    name=src_name,
    version=__version__,
    author=author,
    author_email=author_email,
    long_description=long_distribution,
    discription="a small python package for GAN",
    url=f"http://github.com/{author}/{repo_name}",
    projects_urls={"bug tracker":f"http://github.com/{author}/{repo_name}/issues"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)