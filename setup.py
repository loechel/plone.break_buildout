from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(name='plone.break_buildout',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Buildout :: Extension",
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='zc.buildout Plone break hotfix',
      author='Alexander Loechel',
      author_email='Alexander.Loechel@lmu.de',
      url='https://github.com/collective/plone.break_buildout',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.break_core',
      ],
      entry_points={
        'zc.buildout.extension': ['ext = plone.break_buildout:main'],
      },
      )
