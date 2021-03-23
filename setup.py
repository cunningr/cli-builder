from distutils.core import setup

setup(
    name='tebag',
    packages=[
        'tebag'
    ],
    version='0.0.1',
    license='MIT',
    description='''TEBAG (pronounced Teabag) - Thousand Eyes Bulk API Getter, is 
    a simple CLI tool with an extensible framework for bulk CRUD operations on Thousand Eyes configuration data''',
    author='Richard Cunningham',
    author_email='cunningr@cisco.com',
    url='https://wwwin-github.cisco.com/cxea/tebag',
    download_url='https://wwwin-github.cisco.com/cxea/tebag/archive/master.zip',
    keywords=['Thousand Eyes', 'Observability', 'configuration management'],
    install_requires=[
        'pyyaml',
        'sdtables >= 2.0.0',
        'tabulate',
        'requests',
        'pyfiglet'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ],
    entry_points={
        'console_scripts': [
            'prog = prog.cli:main'
        ]
    }
)
