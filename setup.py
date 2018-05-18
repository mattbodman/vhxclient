from setuptools import setup

setup(name='vhxclient',
      version='1.1',
      description='A Python Client for the VHX API',
      url='https://github.com/mattbodman/vhxclient',
      author='Matt Bodman',
      author_email='matt@acctv.com.au',
      license='MIT',
      packages=['vhxclient'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      dependency_links=['https://github.com/mattbodman/vhxclient/archive/master.zip'], install_requires=['httplib2']
      )
