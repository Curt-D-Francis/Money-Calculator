from appSetup import setup, find_packages

setup(
    name="money-calculator",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'customtkinter>=5.2.2',
        'tk>=0.1.0',
    ],
)