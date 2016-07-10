#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from pycroservices import function

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@function(auto_emit=False)
def split(event, context):
    logger.info("receive={}".format(event))
    words = event.split()
    context.pycro_context.emit(words, context)
    return words


@function()
def count(event, context):
    logger.info("count={}".format(len(event)))
