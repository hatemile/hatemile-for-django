HaTeMiLe for Django
===================

HaTeMiLe for Django improve accessibility of web pages that uses the Django framework, converting pages with HTML code into pages with a more accessible code.

## Accessibility solutions

* [Associate HTML elements](https://github.com/hatemile/hatemile-for-python/wiki/Associate-HTML-elements);
* [Provide a polyfill to CSS Speech and CSS Aural properties](https://github.com/hatemile/hatemile-for-python/wiki/Provide-a-polyfill-to-CSS-Speech-and-CSS-Aural-properties);
* [Display inacessible informations of page](https://github.com/hatemile/hatemile-for-python/wiki/Display-inacessible-informations-of-page);
* [Enable all functionality of page available from a keyboard](https://github.com/hatemile/hatemile-for-python/wiki/Enable-all-functionality-of-page-available-from-a-keyboard);
* [Improve the acessibility of forms](https://github.com/hatemile/hatemile-for-python/wiki/Improve-the-acessibility-of-forms);
* [Provide accessibility resources to navigate](https://github.com/hatemile/hatemile-for-python/wiki/Provide-accessibility-resources-to-navigate).

## Documentation

To generate the full API documentation of HaTeMiLe of Django:

1. [Install, create and activate a virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/);
2. [Install dependencies](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/#using-requirements-files);
3. [Execute the API docs of sphinx in `docs` directory](https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/);
    ```bash
    sphinx-apidoc -e -f -o _modules/ ../hatemile
    make html
    ```
4. Open the `docs/_build/html/index.html` with an internet browser.

## Contributing

If you want contribute with HaTeMiLe for Django, read [contributing guidelines](CONTRIBUTING.md).

## See also
* [HaTeMiLe for CSS](https://github.com/hatemile/hatemile-for-css)
* [HaTeMiLe for JavaScript](https://github.com/hatemile/hatemile-for-javascript)
* [HaTeMiLe for Java](https://github.com/hatemile/hatemile-for-java)
* [HaTeMiLe for PHP](https://github.com/hatemile/hatemile-for-php)
* [HaTeMiLe for Python](https://github.com/hatemile/hatemile-for-python)
* [HaTeMiLe for Ruby](https://github.com/hatemile/hatemile-for-ruby)
