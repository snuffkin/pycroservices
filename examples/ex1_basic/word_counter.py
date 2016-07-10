#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from pycroservices import function

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@function()
def split(event, context):
    logger.info("receive={}".format(event))
    words = event.split()
    return words


@function()
def count(event, context):
    logger.info("count={}".format(len(event)))
