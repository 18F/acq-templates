# templates

A collection of templatized standard 18F documents, written in Markdown and compatible with various templating languages.

## Adding a template

This project is language-agnostic, and thus should be importable as a package in multiple languages. This does mean that we're unable to take advantage of some of the advanced features of templating languages. Instead, the templates should expect basic template fields with the expectation that more advanced logic will happen before templating occurs.

If you are creating a template, please check if there is an existing template type, via the directories. If there is an existing directory to accommodate your template type, please add your template in the respective folder. Please create an issue if your template fields are not covered by the existing sample data `json` in that directory.

If you are creating your own template type, please create a new directory in the top level folder. The directory should include your template in a `.md` file, and a `.json` of sample data for that template.

All templates must be in a [markdown](https://daringfireball.net/projects/markdown/) form using `{{ field }}`-style tags compatile with [Mustache](https://mustache.github.io/), [Handlebars](http://handlebarsjs.com/), [Django](https://docs.djangoproject.com/en/1.10/ref/templates/language/), and [Jinja2](http://jinja.pocoo.org/).

## Installation

### Python

```
pip install acq_templates
```

To use the templates in a Django project, add `acq_templates` to the `INSTALLED_APPS` in `settings.py`.

## Distribution

### Python

Follow the [PyPI upload instructions](https://packaging.python.org/distributing/#uploading-your-project-to-pypi).

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for additional information.

### Branch flow

- Main branch: `release`
- Development branch: `develop`

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.
