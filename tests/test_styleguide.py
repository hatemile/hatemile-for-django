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
Tests of styleguide of HaTeMiLe for Django.
"""

import glob
import os
import unittest
import pycodestyle
from pylint import epylint


class TestStyleguide(unittest.TestCase):
    """
    Check if HaTeMiLe for Django is conformance of own styleguide.
    """

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    PATHS = (
        os.path.join(BASE_DIR, 'tests'),
        os.path.join(BASE_DIR, 'setup.py')
    )

    def test_pep8(self):
        """
        Check if HaTeMiLe for Django is conformance with pep8.
        """

        files = []
        for path in TestStyleguide.PATHS:
            if os.path.isfile(path):
                files.extend([path])
            else:
                files.extend(glob.glob(path + '/**/*.py', recursive=True))

        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(files)
        self.assertEqual(
            result.total_errors,
            0,
            str(result.get_statistics())
        )

    def test_pylint(self):
        """
        Check if HaTeMiLe for Django is conformance with python standarts.
        """

        for path in TestStyleguide.PATHS:
            stdout = epylint.py_run(path + ' --score=n', return_std=True)[0]
            self.assertFalse(stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
