import setuptools
import os, glob

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version():
    import os
    vf = 'version.txt'
    maxversions = [9, 9, 9, 9, 9, 9, 9]

    def add_version(version, index=-1):
        if index == -1: index = len(version) - 1
        version[index] += 1
        if version[index] > maxversions[len(version) - index - 1]:
            version[index] = 0
            if index == 0:
                raise Exception('Max version number reached. %s' % (version))
            return add_version(version, index - 1)
        else:
            return version

    if not os.path.exists(vf):
        raise Exception('version.txt not found or  is invalid')
    with open(vf, 'r') as f:
        numbers = f.read().strip()
        if numbers == '':
            raise Exception('version.txt not found or  is invalid')
        version = numbers.split('.')
        version = [int(x) for x in version]
        version = add_version(version)
        version = '.'.join([str(x) for x in version])

    with open(vf, 'w') as f:
        f.write(version)
    return version


version = get_version()
print("version:", version)
setuptools.setup(
    executable=True,
    name="TestPackageName",  # Replace with your own username
    version=version,
    author="TestAuthor",
    author_email="TestAuthorEmail",
    description="TestPacakgeDescription",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="TestPackageUrl",
    packages=setuptools.find_packages(),
    package_dir={'TestPackageName': 'TestPackageName'},
    install_requires=['jinja2'],
    entry_points={
        'console_scripts': [
            'TestPackageName = TestPackageName.clitools.cli:main',
        ]
    },
    include_package_data=True,
    package_data={
        'TestPackageName': [
            'data/*', 'data/*/*', 'data/*/*/*', 'data/*/*/*/*', 'data/*/*/*/*/*', 'data/*/*/*/*/*/*',
            'data/*/*/*/*/*/*/*',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)