#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'

from pecan import rest
from wsme import types as wtypes
from webdemo.api import expose as webdemo_expose
from webdemo.api.controllers.v1 import users as v1_users


class V1Controller(rest.RestController):
    users = v1_users.UsersController()

    @webdemo_expose.expose(wtypes.text)
    def get(self):
        return 'webdemo v1controller'

