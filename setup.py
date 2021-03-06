from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='goenrich',
      version='1.2.2',
      description='GO enrichment with python -- pandas meets networkx',
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Topic :: Software Development :: Libraries'],
      keywords= ['GO', 'Gene Ontology', 'Biology', 'Enrichment',
          'Bioinformatics', 'Computational Biology',
          'library',
          'visualization', 'graphviz', 'pandas'],
      url='https://github.com/jdrudolph/goenrich',
      author='Jan Daniel Rudolph',
      author_email='jan.daniel.rudolph@gmail.com',
      license='MIT',
      packages=['goenrich'],
      install_requires=[
          'numpy',
          'pandas',
          'scipy',
          'statsmodels',
          'networkx'],
      test_suite='nose.collector',
      tests_require=['nose', 'setuptools'],
      zip_safe=False)
