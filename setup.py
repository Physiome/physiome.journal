from setuptools import setup
from setuptools import find_packages

version = '0.0'

classifiers = """
Development Status :: 4 - Beta
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)
Operating System :: OS Independent
Programming Language :: JavaScript
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
""".strip().splitlines()

package_json = {
    "dependencies": {
    },
    "devDependencies": {
    }
}

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(
    name='physiome.journal',
    version=version,
    description="Physiome Journal support package",
    long_description=long_description,
    classifiers=classifiers,
    keywords='',
    author='Tommy Yu',
    author_email='tommy.yu@auckland.ac.nz',
    url='https://github.com/Physiome/physiome.journal',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['physiome'],
    zip_safe=False,
    include_package_data=True,
    package_json=package_json,
    install_requires=[
        'markdown',
        'Jinja2>=2.4',

        'calmjs>=3.4.1',
        'calmjs.sassy[libsass]',

        'nunja'
        ' @ git+https://github.com/metatoaster/nunja.git@nunja_jinja',
        'repodono.model[flask] '
        ' @ git+https://github.com/repodono/repodono.model.git@demo',
        'repodono.task'
        ' @ git+https://github.com/repodono/repodono.task.git@master',
        'repodono.nunja'
        ' @ git+https://github.com/repodono/repodono.nunja.git@master',
    ],
    python_requires='>=3.6',
    extras_require={},
    build_calmjs_artifacts=True,
    entry_points={
        'nunja.mold': [
            'physiome.journal.molds = physiome.journal:molds',
        ],
        'nunja.tmpl': [
            'physiome.journal.templates = physiome.journal:templates',
        ],
        'calmjs.module': [
            'physiome.journal = physiome.journal',
        ],
        'calmjs.scss': [
            'physiome.journal = physiome.journal',
        ],
        'calmjs.artifacts': [
            'styles.css = calmjs.sassy.artifact:complete_css',
            'styles.min.css = calmjs.sassy.artifact:complete_compressed_css',
        ],
    },
    test_suite="physiome.journal.tests.make_suite",
)
