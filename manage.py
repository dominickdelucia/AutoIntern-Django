#!/usr/bin/env python
# Copyright 2015 Google Inc.
#
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

import os
import sys

if __name__ == "__main__":
    SETTINGS = "mysite.settings.base"
    try:
        if os.environ["ENVIRONMENT"] == 'UAT':
            SETTINGS = "mysite.settings.uat"
        if os.environ["ENVIRONMENT"] == 'PROD':
            SETTINGS = "mysite.settings.prod"
    except KeyError as ke:
        # Assume this ok and using the default settings
        pass

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS)
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
