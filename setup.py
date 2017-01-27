import os
import re
import shutil
import inflection
from setuptools import setup, find_packages

# Convert Markdown README into reStructured Text
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

# Create Django-relevant folders
if os.path.exists('acq_templates'):
    shutil.rmtree('acq_templates')
if os.path.exists('acq_templates.egg-info'):
    shutil.rmtree('acq_templates.egg-info')
if os.path.exists('build'):
    shutil.rmtree('build')
if os.path.exists('dist'):
    shutil.rmtree('dist')
django_path = 'acq_templates/templates/acq_templates/'
here = os.scandir('.')


for entry in here:
    if not os.path.exists(django_path):
        os.makedirs(django_path)

    if not entry.name.startswith('.') and entry.is_dir():
        shutil.copytree(
            src=entry.name,
            dst=django_path + entry.name
        )


# Convert camelcased fields into underscore
def convert_underscore(file):
    with open(file, 'r+') as f:
        content = f.read()
        content = re.sub(
            r'{{ (.+)? }}',
            lambda x: inflection.underscore(x.group()),
            content
        )
        f.seek(0)
        f.write(content)
        f.truncate()

for root, dirs, files in os.walk(django_path):
    for file in files:
        if file.endswith(".md"):
            convert_underscore(os.path.join(root, file))

setup(
    name='acq_templates',
    version='0.1.2',
    url='https://github.com/18F/acq-templates',
    license='CC0-1.0',
    description='Markdown templates designed for acquisitions by the United '
                'States government.',
    long_description=read_md('README.md'),
    author='TTS Office of Acquisitions',
    author_email='',
    packages=['acq_templates'],
    package_data={
        'acq_templates': ['acq_templates/*']
    },
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
