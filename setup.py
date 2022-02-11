from pydoc import cli
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name = 'traceable-cli',
    version = '0.0.6',
    author = 'Saad Farooq',
    author_email = 'saad@traceable.ai',
    license = 'MIT',
    description = 'Tool to install the Traceable Platform agent as well as the Traceable NGINX Agent',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/shloth/traceable-cli.git',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires = ['click>=7.1.2', 'requests>=2.26.0'],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",      
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",   
    ],

    entry_points = {
        'console_scripts': [
            'traceable-cli=cli.cli:cli',
        ],
    }
)
