# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Module of AccessibleDjangoMiddleware class.
"""

from django.conf import settings
from hatemile.implementation.assoc import AccessibleAssociationImplementation
from hatemile.implementation.css import AccessibleCSSImplementation
from hatemile.implementation.display import AccessibleDisplayImplementation
from hatemile.implementation.event import AccessibleEventImplementation
from hatemile.implementation.form import AccessibleFormImplementation
from hatemile.implementation.navig import AccessibleNavigationImplementation
from hatemile.util.configure import Configure
from hatemile.util.css.tinycss.tinycssparser import TinyCSSParser
from hatemile.util.html.bs.bshtmldomparser import BeautifulSoupHTMLDOMParser


#: Parameter to execute the associate_all_data_cells_with_header_cells method
ASSOCIATE_TABLES = 'associate-all-data-cells-with-header-cells'

#: Parameter to execute the associate_all_labels_with_fields method
ASSOCIATE_LABELS = 'associate-all-labels-with-fields'

#: Parameter to execute the provide_all_speak_properties method
SUPPORT_CSS_SPEAK = 'provide-all-speak-properties'

#: Parameter to execute the display_all_alternative_text_images method
DISPLAY_ALTERNATIVE_TEXTS = 'display-all-alternative-text-images'

#: Parameter to execute the display_all_cell_headers method
DISPLAY_CELL_HEADERS = 'display-all-cell-headers'

#: Parameter to execute the display_all_languages method
DISPLAY_LANGUAGES = 'display-all-languages'

#: Parameter to execute the display_all_links_attributes method
DISPLAY_LINK_ATTRIBUTES = 'display-all-links-attributes'

#: Parameter to execute the display_all_roles method
DISPLAY_ROLES = 'display-all-roles'

#: Parameter to execute the display_all_titles method
DISPLAY_TITLES = 'display-all-titles'

#: Parameter to execute the display_all_shortcuts method
DISPLAY_SHORTCUTS = 'display-all-shortcuts'

#: Parameter to execute the display_all_wai_aria_states method
DISPLAY_WAI_ARIA_STATES = 'display-all-wai-aria-states'

#: Parameter to execute the make_accessible_all_click_events method
ENABLE_CLICK_EVENTS = 'make-accessible-all-click-events'

#: Parameter to execute the make_accessible_all_drag_and_drop_events method
ENABLE_DRAG_AND_DROP_EVENTS = 'make-accessible-all-drag-and-drop-events'

#: Parameter to execute the make_accessible_all_hover_events method
ENABLE_HOVER_EVENTS = 'make-accessible-all-hover-events'

#: Parameter to execute the mark_all_autocomplete_fields method
MARK_AUTOCOMPLETE_FIELDS = 'mark-all-autocomplete-fields'

#: Parameter to execute the mark_all_range_fields method
MARK_RANGE_FIELDS = 'mark-all-range-fields'

#: Parameter to execute the mark_all_required_fields method
MARK_REQUIRED_FIELDS = 'mark-all-required-fields'

#: Parameter to execute the mark_all_invalid_fields method
MARK_INVALID_FIELDS = 'mark-all-invalid-fields'

#: Parameter to execute the provide_navigation_to_all_long_descriptions method
CREATE_LINKS_FOR_LONGDESCS = 'provide-navigation-to-all-long-descriptions'

#: Parameter to execute the provide_navigation_by_all_headings method
CREATE_TABLES_OF_CONTENT = 'provide-navigation-by-all-headings'

#: Parameter to execute the provide_navigation_by_all_skippers method
CREATE_SKIPPERS_LIST = 'provide-navigation-by-all-skippers'

#: Parameter to execute the hide_hatemile_changes method
HIDE_HATEMILE_CHANGES = 'hide-hatemile-changes'


#: The default parameters of HaTeMiLe for Django.
DEFAULT_PARAMETERS = {
    ASSOCIATE_TABLES: True,
    ASSOCIATE_LABELS: True,
    SUPPORT_CSS_SPEAK: False,
    DISPLAY_ALTERNATIVE_TEXTS: True,
    DISPLAY_CELL_HEADERS: True,
    DISPLAY_LANGUAGES: True,
    DISPLAY_LINK_ATTRIBUTES: True,
    DISPLAY_ROLES: True,
    DISPLAY_TITLES: True,
    DISPLAY_SHORTCUTS: True,
    DISPLAY_WAI_ARIA_STATES: True,
    ENABLE_CLICK_EVENTS: True,
    ENABLE_DRAG_AND_DROP_EVENTS: True,
    ENABLE_HOVER_EVENTS: True,
    MARK_AUTOCOMPLETE_FIELDS: True,
    MARK_RANGE_FIELDS: True,
    MARK_REQUIRED_FIELDS: True,
    MARK_INVALID_FIELDS: True,
    CREATE_LINKS_FOR_LONGDESCS: True,
    CREATE_TABLES_OF_CONTENT: True,
    CREATE_SKIPPERS_LIST: True,
    HIDE_HATEMILE_CHANGES: True
}


def get_complete_parameters():
    """
    The parameters defined by user and if not set the default parameters.

    :return: The parameters of HaTeMiLe for Django.
    :rtype: dict(str, bool)
    """

    parameters = getattr(settings, 'DEFAULT_PARAMETERS', DEFAULT_PARAMETERS)
    if parameters is not DEFAULT_PARAMETERS:
        if ASSOCIATE_TABLES not in parameters:
            parameters[ASSOCIATE_TABLES] = DEFAULT_PARAMETERS[ASSOCIATE_TABLES]
        if ASSOCIATE_LABELS not in parameters:
            parameters[ASSOCIATE_LABELS] = DEFAULT_PARAMETERS[ASSOCIATE_LABELS]
        if SUPPORT_CSS_SPEAK not in parameters:
            parameters[SUPPORT_CSS_SPEAK] = (
                DEFAULT_PARAMETERS[SUPPORT_CSS_SPEAK]
            )
        if DISPLAY_ALTERNATIVE_TEXTS not in parameters:
            parameters[DISPLAY_ALTERNATIVE_TEXTS] = (
                DEFAULT_PARAMETERS[DISPLAY_ALTERNATIVE_TEXTS]
            )
        if DISPLAY_CELL_HEADERS not in parameters:
            parameters[DISPLAY_CELL_HEADERS] = (
                DEFAULT_PARAMETERS[DISPLAY_CELL_HEADERS]
            )
        if DISPLAY_LANGUAGES not in parameters:
            parameters[DISPLAY_LANGUAGES] = (
                DEFAULT_PARAMETERS[DISPLAY_LANGUAGES]
            )
        if DISPLAY_LINK_ATTRIBUTES not in parameters:
            parameters[DISPLAY_LINK_ATTRIBUTES] = (
                DEFAULT_PARAMETERS[DISPLAY_LINK_ATTRIBUTES]
            )
        if DISPLAY_ROLES not in parameters:
            parameters[DISPLAY_ROLES] = DEFAULT_PARAMETERS[DISPLAY_ROLES]
        if DISPLAY_TITLES not in parameters:
            parameters[DISPLAY_TITLES] = DEFAULT_PARAMETERS[DISPLAY_TITLES]
        if DISPLAY_SHORTCUTS not in parameters:
            parameters[DISPLAY_SHORTCUTS] = (
                DEFAULT_PARAMETERS[DISPLAY_SHORTCUTS]
            )
        if DISPLAY_WAI_ARIA_STATES not in parameters:
            parameters[DISPLAY_WAI_ARIA_STATES] = (
                DEFAULT_PARAMETERS[DISPLAY_WAI_ARIA_STATES]
            )
        if ENABLE_CLICK_EVENTS not in parameters:
            parameters[ENABLE_CLICK_EVENTS] = (
                DEFAULT_PARAMETERS[ENABLE_CLICK_EVENTS]
            )
        if ENABLE_DRAG_AND_DROP_EVENTS not in parameters:
            parameters[ENABLE_DRAG_AND_DROP_EVENTS] = (
                DEFAULT_PARAMETERS[ENABLE_DRAG_AND_DROP_EVENTS]
            )
        if ENABLE_HOVER_EVENTS not in parameters:
            parameters[ENABLE_HOVER_EVENTS] = (
                DEFAULT_PARAMETERS[ENABLE_HOVER_EVENTS]
            )
        if MARK_AUTOCOMPLETE_FIELDS not in parameters:
            parameters[MARK_AUTOCOMPLETE_FIELDS] = (
                DEFAULT_PARAMETERS[MARK_AUTOCOMPLETE_FIELDS]
            )
        if MARK_RANGE_FIELDS not in parameters:
            parameters[MARK_RANGE_FIELDS] = (
                DEFAULT_PARAMETERS[MARK_RANGE_FIELDS]
            )
        if MARK_REQUIRED_FIELDS not in parameters:
            parameters[MARK_REQUIRED_FIELDS] = (
                DEFAULT_PARAMETERS[MARK_REQUIRED_FIELDS]
            )
        if MARK_INVALID_FIELDS not in parameters:
            parameters[MARK_INVALID_FIELDS] = (
                DEFAULT_PARAMETERS[MARK_INVALID_FIELDS]
            )
        if CREATE_LINKS_FOR_LONGDESCS not in parameters:
            parameters[CREATE_LINKS_FOR_LONGDESCS] = (
                DEFAULT_PARAMETERS[CREATE_LINKS_FOR_LONGDESCS]
            )
        if CREATE_TABLES_OF_CONTENT not in parameters:
            parameters[CREATE_TABLES_OF_CONTENT] = (
                DEFAULT_PARAMETERS[CREATE_TABLES_OF_CONTENT]
            )
        if CREATE_SKIPPERS_LIST not in parameters:
            parameters[CREATE_SKIPPERS_LIST] = (
                DEFAULT_PARAMETERS[CREATE_SKIPPERS_LIST]
            )
        if HIDE_HATEMILE_CHANGES not in parameters:
            parameters[HIDE_HATEMILE_CHANGES] = (
                DEFAULT_PARAMETERS[HIDE_HATEMILE_CHANGES]
            )
    return parameters


def execute_hatemile(html_code, current_url, parameters):
    """
    Execute the HaTeMiLe for Python for current HTML code.

    :param html_code: The current HTML code.
    :type html_code: str
    :param current_url: The current URL of request.
    :type current_url: str
    :param parameters: The parameter for execute accessible solutions of
                       HaTeMiLe for Django.
    :type parameters: dict(str, bool)
    :return: A HTML code more accessible
    :rtype: str
    """

    configure = Configure()

    parser = BeautifulSoupHTMLDOMParser(html_code)

    navigation = AccessibleNavigationImplementation(parser, configure)
    display = AccessibleDisplayImplementation(parser, configure)

    if (
        (parameters[ENABLE_DRAG_AND_DROP_EVENTS])
        or (parameters[ENABLE_CLICK_EVENTS])
        or (parameters[ENABLE_HOVER_EVENTS])
    ):
        event = AccessibleEventImplementation(parser)
        if parameters[ENABLE_DRAG_AND_DROP_EVENTS]:
            event.make_accessible_all_drag_and_drop_events()
        if parameters[ENABLE_CLICK_EVENTS]:
            event.make_accessible_all_click_events()
        if parameters[ENABLE_HOVER_EVENTS]:
            event.make_accessible_all_hover_events()

    if (
        (parameters[MARK_REQUIRED_FIELDS])
        or (parameters[MARK_RANGE_FIELDS])
        or (parameters[MARK_AUTOCOMPLETE_FIELDS])
        or (parameters[MARK_INVALID_FIELDS])
    ):
        form = AccessibleFormImplementation(parser)
        if parameters[MARK_REQUIRED_FIELDS]:
            form.mark_all_required_fields()
        if parameters[MARK_RANGE_FIELDS]:
            form.mark_all_range_fields()
        if parameters[MARK_AUTOCOMPLETE_FIELDS]:
            form.mark_all_autocomplete_fields()
        if parameters[MARK_INVALID_FIELDS]:
            form.mark_all_invalid_fields()

    if parameters[CREATE_TABLES_OF_CONTENT]:
        navigation.provide_navigation_by_all_headings()
    if parameters[CREATE_SKIPPERS_LIST]:
        navigation.provide_navigation_by_all_skippers()
    if parameters[CREATE_LINKS_FOR_LONGDESCS]:
        navigation.provide_navigation_to_all_long_descriptions()

    if (
        (parameters[ASSOCIATE_TABLES])
        or (parameters[ASSOCIATE_LABELS])
    ):
        association = AccessibleAssociationImplementation(parser)
        if parameters[ASSOCIATE_TABLES]:
            association.associate_all_data_cells_with_header_cells()
        if parameters[ASSOCIATE_LABELS]:
            association.associate_all_labels_with_fields()

    if parameters[SUPPORT_CSS_SPEAK]:
        css_parser = TinyCSSParser(parser, current_url)
        css = AccessibleCSSImplementation(
            parser,
            css_parser,
            configure
        )
        css.provide_all_speak_properties()

    if parameters[DISPLAY_SHORTCUTS]:
        display.display_all_shortcuts()
    if parameters[DISPLAY_ROLES]:
        display.display_all_roles()
    if parameters[DISPLAY_CELL_HEADERS]:
        display.display_all_cell_headers()
    if parameters[DISPLAY_WAI_ARIA_STATES]:
        display.display_all_waiaria_states()
    if parameters[DISPLAY_LINK_ATTRIBUTES]:
        display.display_all_links_attributes()
    if parameters[DISPLAY_TITLES]:
        display.display_all_titles()
    if parameters[DISPLAY_LANGUAGES]:
        display.display_all_languages()
    if parameters[DISPLAY_ALTERNATIVE_TEXTS]:
        display.display_all_alternative_text_images()

    if parameters[CREATE_SKIPPERS_LIST]:
        navigation.provide_navigation_by_all_skippers()

    if parameters[DISPLAY_SHORTCUTS]:
        display.display_all_shortcuts()

    return parser.get_html()


class AccessibleDjangoMiddleware:
    """
    The AccessibleDjangoMiddleware convert a HTML code in a HTML code more
    accessible for Django projects.
    """

    def __init__(self, get_response):
        """
        Instanciate a new middleware that convert a HTML code in a HTML code
        more accessible for Django projects.

        :param get_response: A function that returns the django response.
        :type get_response: function
        """

        self.get_response = get_response

    def __call__(self, request):
        """
        Execute the HaTeMiLe for Python for each request.

        :param request: The request.
        :type request: django.http.HttpRequest
        """

        response = self.get_response(request)

        content_type = response['Content-Type'].replace(' ', '').replace(
            'charset=',
            ''
        )
        if ';' in content_type:
            mime_type, encoding = content_type.split(';')
        else:
            mime_type = None
            encoding = None

        if (not response.streaming) and (mime_type == 'text/html'):
            html_code = response.content.decode(encoding)
            current_url = request.build_absolute_uri(request.get_full_path())
            parameters = get_complete_parameters()

            new_html_code = execute_hatemile(
                html_code,
                current_url,
                parameters
            )

            response.content = new_html_code.encode(encoding)

        return response
