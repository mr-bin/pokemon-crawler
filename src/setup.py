from setuptools import find_packages, setup

tests_require = ["pytest", "black", "pylint", "isort", "flake8", "mypy"]

setup(
    name="pokemon_crawler",
    version="0.0.1",
    author="mr_bin",
    description="",
    license="Private",
    url="https://github.com/mr-bin/pokemon_crawler",
    packages=find_packages(),
    package_data={"": ["*.sh", "*.ini", "*.pem", "*.txt"], "configs": ["*.yaml"]},
    install_requires=["PyYAML", "Django", "requests", "psycopg2-binary", "tzdata"],
    extras_require={
        "tests": tests_require,
    },
    entry_points={
        "console_scripts": [
            "manage.py = pokemon_crawler.manage:main",
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "License :: Other/Proprietary License",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
    ],
)
