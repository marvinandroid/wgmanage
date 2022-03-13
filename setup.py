from setuptools import setup, find_packages

from wgmanage.core import get_version, DESCRIPTION

setup(
    name='wgmanage',
    version=get_version(),
    description=DESCRIPTION,
    packages=find_packages(),
    url='https://github.com/marvinandroid/wgmanage',
    license='GPLv3',
    author='Alexander Zakharov',
    author_email='me@marvinknoxville.wtf',
    package_data={'wgmanage': ['templates/*.j2']},
    entry_points={
        'console_scripts': [
            'wgmanage=wgmanage:main'
        ],
        'wgmanage.cli': [

        ]
    }
)
