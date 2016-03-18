#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'

import wsmeext.pecan as wsme_pecan
from pecan import rest
from wsme import types as wtypes
from webdemo.api import expose as webdemo_expose
from webdemo.api.controllers.v1 import controller as v1_controller


class RootController(rest.RestController):
    v1 = v1_controller.V1Controller()

    @webdemo_expose.expose(wtypes.text)
    def get(self):
        return "webdemo"
