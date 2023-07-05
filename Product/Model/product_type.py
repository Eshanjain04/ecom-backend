# -*- coding: utf-8 -*-
import mongoengine as me

from utilities.DocumentCreate import DocumentCreate


class Category(DocumentCreate):
    name = me.StringField(required=True)
