#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Copyright 2016 Satoyuki Tsukano

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import json
import logging
import pycroservices
import sys


def _get_target_method(name):
    with open(name + '.json', mode='r') as f:
        config = json.load(f)
    handler = config['handler']

    [module_name, attr_name] = handler.split('.')
    mod = __import__(module_name)
    return getattr(mod, attr_name)

if __name__ == "__main__":
    target_method = _get_target_method(sys.argv[1])
    with open('event.json', mode='r') as f:
        event = json.load(f)
    context = pycroservices.LocalContext(sys.argv[1])
    target_method(event, context)
