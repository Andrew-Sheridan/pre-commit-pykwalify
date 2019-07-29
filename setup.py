from setuptools import find_packages, setup

setup(
    name="pykwalify-validate",
    version="0.0.0",
    author="Andrew Sheridan",
    description="",
    long_description="",
    license="",
    keywords=['yaml', 'lint', 'linter', 'syntax', 'checker'],
    url='https://github.com/Andrew-Sheridan/pre-commit-pykwalify',
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(),
    entry_points={'console_scripts': ['pykwalify-validate=pykwalify_validate.cli:main']},
    install_requires=["PyYAML", "pykwalify"],
    test_suite='tests',
)
