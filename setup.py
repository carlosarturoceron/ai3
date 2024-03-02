import setuptools

setuptools.setup(
    name="ai3",
    version="0.0.0",
    author="Carlos Linares",
    author_email="oddskid@gmail.com",
    url="https://github.com/carlosarturoceron/ai3",
    packages=setuptools.find_packages(),
    install_requires = [
        "requests",
        "tensorflow==2.13.1"
    ],
    python_requires =">=3.8",
    include_package_data=True
)