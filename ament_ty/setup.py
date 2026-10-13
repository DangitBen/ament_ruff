from setuptools import find_packages, setup

package_name = 'ament_ty'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'argcomplete',
        'ty',
        'setuptools',
    ],
    package_data={
        '': [
            'configuration/ty.toml',
        ],
    },
    zip_safe=True,
    maintainer='Ben Andrew',
    maintainer_email='benjamin.andrew@swri.org',
    description='Python type checker using ty',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['ament_ty = ament_ty.main:main'],
        'pytest11': [
            'ament_ty = ament_ty.pytest_marker',
        ],
    },
)
