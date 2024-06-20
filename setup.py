from io import open
from setuptools import setup
from dl_train_gui import __version__ as version

setup(
    name='Alanta',
    version=version,
    url='https://github.com/VishwanathTanmai',
    license='Apache 2.0',
    author='vishwanath',
    description='Python <-> HTML/Alanta.',
    long_description=''.join(open('README.md', encoding='utf-8').readlines()),
    long_description_content_type='text/markdown',
    keywords=['gui', 'executable'],
    packages=['alanta'],
    include_package_data=True,
    install_requires=['eel==0.14.0'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'dover=dover.__main__:run',
            'dover=dover.__main__:run',
        ]
    }
)