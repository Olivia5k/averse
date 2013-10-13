from distutils.core import setup


setup(
    name='averse',
    version='0.1',  # The cobbler's children have no shoes :>
    url='https://github.com/thiderman/averse',
    author='Lowe Thiderman',
    author_email='lowe.thiderman@gmail.com',
    description=('git based automatic versioning'),
    license='Public Domain',
    packages=['averse'],
    scripts=[
        'bin/averse'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: Public Domain',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Version Control',
    ],
)
