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
Module to setup HaTeMiLe for Django.
"""

import os
from setuptools import find_packages
from setuptools import setup


BASE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def get_long_description():
    """
    Returns the long description of HaTeMiLe for Django.

    :return: The long description of HaTeMiLe for Django.
    :rtype: str
    """

    with open(
        os.path.join(BASE_DIRECTORY, 'README.md'),
        'r',
        encoding='utf-8'
    ) as readme_file:
        return readme_file.read()


def get_requirements():
    """
    Returns the content of 'requirements.txt' in a list.

    :return: The content of 'requirements.txt'.
    :rtype: list(str)
    """

    requirements = []
    with open(
        os.path.join(BASE_DIRECTORY, 'requirements.txt'),
        'r',
        encoding='utf-8'
    ) as requirements_file:
        lines = requirements_file.readlines()
        for line in lines:
            requirements.append(line.strip())
    return requirements


def get_requirements_dev():
    """
    Returns the content of 'requirements-dev.txt' in a list.

    :return: The content of 'requirements-dev.txt'.
    :rtype: list(str)
    """

    requirements = []
    with open(
        os.path.join(BASE_DIRECTORY, 'requirements-dev.txt'),
        'r',
        encoding='utf-8'
    ) as requirements_file:
        lines = requirements_file.readlines()
        for line in lines:
            requirements.append(line.strip())
    return requirements


setup(
    name='hatemile-for-django',
    description=(
        'HaTeMiLe for Django improve accessibility of web pages that uses the '
        + 'Django framework, converting pages with HTML code into pages with '
        + 'a more accessible code.'
    ),
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    version='1.0.0',
    url='https://github.com/hatemile/hatemile-for-django',
    author='Carlson Santana Cruz',
    license='Apache2',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Natural Language :: English'
    ],
    packages=find_packages(),
    install_requires=get_requirements(),
    extras_require={
        'dev': get_requirements_dev()
    }
)
