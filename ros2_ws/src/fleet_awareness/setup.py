from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'fleet_awareness'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py'),
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mahmoudemad',
    maintainer_email='mahmoudemad@todo.todo',
    description='Traffic System',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'fleet_emulator = fleet_awareness.fleet_emulator2:main',
            'traffic_manager = fleet_awareness.traffic_manager2:main',
        ],
    },
)