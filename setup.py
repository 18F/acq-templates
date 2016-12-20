from setuptools import setup, find_packages

try:
    from pypandoc import convert

    def read_md(f):
        return convert(
            f,
            to='rst',
            format='markdown_github'
        )
except ImportError:
    print("warning: pypandoc module not found, "
          "could not convert Markdown to RST")

    def read_md(f):
        return open(f, 'r', encoding='utf-8').read()

setup(
    name='acq_templates',
    version='0.1.0',
    url='https://github.com/18F/acq-templates',
    license='CC0-1.0',
    description='Markdown templates designed for acquisitions by the United '
                'States government.',
    long_description=read_md('README.md'),
    author='TTS Office of Acquisitions',
    author_email='',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.4',
        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
