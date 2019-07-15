#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    forms.py
   @Desc:     
   @Author:   CE SLT-Auto
   @Create:   2019.07.04   14:21
-------------------------------------------------------------------------------
   @Change:   2019.07.04
-------------------------------------------------------------------------------
"""

from django import forms
from models import ToDo


class ToDoPostForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('content',)

