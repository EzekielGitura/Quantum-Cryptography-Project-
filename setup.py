from setuptools import setup, find_packages

setup(
    name='quantum-crypto-system',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'qiskit>=0.36.0',
        'numpy>=1.22.3',
        'cryptography>=3.4.7',
        'quantum-random>=1.0.3'
    ],
    author='Ezekiel Waweru',
    author_email='gituraezekiel@gmail.com',
    description='Quantum Cryptography System',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/quantum-crypto-system',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Topic :: Security :: Cryptography'
    ]
)
