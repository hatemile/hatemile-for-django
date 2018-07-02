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

## Usage

Add HaTeMiLe for Django in `INSTALLED_APPS` of `settings.py`, to load the stylesheet that hide visual changes of library and the scripts used in events.

```python
INSTALLED_APPS = [
    # ...
    'hatemile_for_django',
]
```

Add the middleware of HaTeMiLe for Django in `MIDDLEWARE_CLASSES` of `settings.py`.

```python
MIDDLEWARE_CLASSES = (
    # ...
    'hatemile_for_django.middleware.AccessibleDjangoMiddleware',
)

You can control which are solutions will be executed, add the dict `HATEMILE_PARAMETERS` in `settings.py`.

```python
HATEMILE_PARAMETERS = {
    # Associate all data cells with header cells of all tables.
    'associate-all-data-cells-with-header-cells': True,
    # Associate all labels with fields.
    'associate-all-labels-with-fields': True,
    # Provide the CSS features of speaking and speech properties in all
    # elements.
    'provide-all-speak-properties': False,
    # Display the alternative text of all images.
    'display-all-alternative-text-images': True,
    # Display the headers of each data cell of all tables.
    'display-all-cell-headers': True,
    # Display the language of all elements.
    'display-all-languages': True,
    # Display the attributes of all links.
    'display-all-links-attributes': True,
    # Display the WAI-ARIA roles of all elements.
    'display-all-roles': True,
    # Display the titles of all elements.
    'display-all-titles': True,
    # Display all shortcuts.
    'display-all-shortcuts': True,
    # Display the WAI-ARIA attributes of all elements.
    'display-all-wai-aria-states': True,
    # Make all click events available from a keyboard.
    'make-accessible-all-click-events': True,
    # Make all Drag-and-Drop events available from a keyboard.
    'make-accessible-all-drag-and-drop-events': True,
    # Make all hover events available from a keyboard.
    'make-accessible-all-hover-events': True,
    # Mark that the fields have autocomplete.
    'mark-all-autocomplete-fields': True,
    # Mark that the fields have range.
    'mark-all-range-fields': True,
    # Mark that the fields is required.
    'mark-all-required-fields': True,
    # Mark a solution to display that a fields are invalid.
    'mark-all-invalid-fields': True,
    # Provide an alternative way to access the longs descriptions of all
    # elements.
    'provide-navigation-to-all-long-descriptions': True,
    # Provide navigation by headings.
    'provide-navigation-by-all-headings': True,
    # Provide navigation by content skippers.
    'provide-navigation-by-all-skippers': True,
    # Hide visual changes of HaTeMiLe.
    'hide-hatemile-changes': True,
}
```

## Contributing

If you want contribute with HaTeMiLe for Django, read [contributing guidelines](https://github.com/hatemile/hatemile-for-django/blob/master/CONTRIBUTING.md).

## See also
* [HaTeMiLe for CSS](https://github.com/hatemile/hatemile-for-css)
* [HaTeMiLe for JavaScript](https://github.com/hatemile/hatemile-for-javascript)
* [HaTeMiLe for Java](https://github.com/hatemile/hatemile-for-java)
* [HaTeMiLe for PHP](https://github.com/hatemile/hatemile-for-php)
* [HaTeMiLe for Python](https://github.com/hatemile/hatemile-for-python)
* [HaTeMiLe for Ruby](https://github.com/hatemile/hatemile-for-ruby)
