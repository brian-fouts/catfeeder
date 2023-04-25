import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="catfeeder",
        url="https://github.com/brian-fouts/catfeeder",
        author="Brian Fouts",
        packages=setuptools.find_packages(),
        include_package_data=True,
        install_requires=[
            "pyyaml",
            #"RPi.GPIO"
        ],
        extras_require={
            "test": [
                "pytest",
                "pytest-cov",
                "pytest-mock",
                "flake8",
                "mypy",
                "black",
                "isort",
            ],
        },
        entry_points=dict(
            console_scripts="catfeeder=catfeeder.__main__:main"
        )
    )

