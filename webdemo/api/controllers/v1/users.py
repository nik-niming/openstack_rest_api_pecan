#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'

import pecan
from pecan import rest
from wsme import types as wtypes
from webdemo.api import expose as webdemo_expose

user_info_list = [
    {
        'id': '1',
        'name': 'Alice',
        'age': 30,
    },
    {
        'id': '2',
        'name': 'Bob',
        'age': 40,
    }
]

class User(wtypes.Base):
    id = wtypes.wsattr(wtypes.text, mandatory=True)
    name = wtypes.text
    age = int


class Users(wtypes.Base):
    users = [User]


class UserController(rest.RestController):

    def __init__(self,user_id):
        self.user_id = user_id

    @webdemo_expose.expose(User)
    def get(self):
        for user_info in user_info_list:
            if user_info['id'] == self.user_id:
                return User(**user_info)

    @webdemo_expose.expose()
    def delete(self):
        for user_info in user_info_list:
            if user_info['id'] == self.user_id:
                user_info_list.remove(user_info)


class UsersController(rest.RestController):
    @pecan.expose()
    def _lookup(self, user_id, *remainder):
        return UserController(user_id), remainder

    @webdemo_expose.expose(Users)
    def get(self):
        user_list = [User(**user_info) for user_info in user_info_list]
        return Users(users=user_list)

    @webdemo_expose.expose(None, body=User, status_code=201)
    def post(self, user):
        user_info = dict()
        user_info['id'] = user.id
        user_info['name'] = user.name
        user_info['age'] = user.age
        user_info_list.append(user_info)
