from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'traceable-cli',
    version = '0.0.5',
    author = 'Saad Farooq',
    author_email = 'saad@traceable.ai',
    license = 'MIT',
    description = 'Tool to install the Traceable Platform agent as well as the Traceable NGINX Agent',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/shloth/traceable-cli.git',
    py_modules = ['traceable_cli', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",      
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",   
    ],
    entry_points = '''
        [console_scripts]
        traceable-cli=traceable_cli:cli
    '''
)
