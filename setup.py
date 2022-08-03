from setuptools import setup

setup(
    name='Flask_Boto3',
    version='0.3.4',
    url='https://github.com/Ketouem/flask-boto3',
    license='MIT',
    author='Cyril "Ketouem" Thomas',
    author_email='ketouem@gmail.com',
    description='Flask extension that ties boto3 to the application',
    packages=['flask_boto3'],
    zip_safe=False,
    include_package_data=True,
    test_suite='tests',
    install_requires=['Flask', 'boto3'],
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
