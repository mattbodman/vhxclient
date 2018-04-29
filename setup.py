from setuptools import setup

setup(name='vhxclient',
      version='0.1',
      description='A Python Client for the VHX API',
      url='',
      author='Matt Bodman',
      author_email='matt@acctv.com.au',
      license='MIT',
      packages=['vhxclient'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose']
      )
