import setuptools

setuptools.setup(
    name="ai3",
    version="0.0.1",
    author="Carlos Linares",
    author_email="oddskid@gmail.com",
    url="https://github.com/carlosarturoceron/ai3",
    packages=setuptools.find_packages(),
    install_requires = [
        "requests",
        "tensorflow==2.12.0",
        "h5py==3.10.0",
        "requests==2.31.0",
        "requests-oauthlib==1.3.1",
        "requests-toolbelt==1.0.0",
        "tensorboard===2.12.3",
        "tensorboard-data-server==0.7.2",
        "tensorflow==2.12.0",
        "tensorflow-estimator==2.12.0",
        "tensorflow-io-gcs-filesystem==0.34.0",
        "oauthlib==3.2.2"
    ],
    python_requires =">=3.8",
    include_package_data=True
)