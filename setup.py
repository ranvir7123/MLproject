from setuptools import find_packages, setup

setup(
    name='MLproject',
    version='1.0',
    packages=find_packages(where='src'),  # <- Tells setuptools to look in src/
    package_dir={'': 'src'},              # <- Maps root to src/
    install_requires=[
        'pandas',
        'numpy',
        'seaborn'
    ]
)
