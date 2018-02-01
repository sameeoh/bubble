# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    address = models.ForeignKey(Address, related_name='user')
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    special = models.TextField(default="None")
    method = models.CharField(max_length=10)
    method_date = models.DateField(default=datetime.date.today)
    customer = models.ForeignKey(User, related_name="orders")
    status = models.CharField(max_length=25, default="New")
    total = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    product = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    price = models.FloatField()
    order = models.ManyToManyField(Order, through='ListItems', related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ListItems(models.Model):
    order = models.ForeignKey(Order, related_name="list_items")
    product = models.ForeignKey(Product, related_name="list_items")
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
