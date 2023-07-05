# -*- coding: utf-8 -*-
import mongoengine as me

from utilities.DocumentCreate import DocumentCreate


class Product(DocumentCreate):
    name = me.StringField(max_length=100, required=True)
    description = me.StringField()
    category = me.ReferenceField('Category', reverse_delete_rule=me.DENY, required=True)
    stock = me.FloatField(required=True)
    weight = me.StringField(required=True)
    price = me.FloatField(required=True)
    image = me.StringField()
