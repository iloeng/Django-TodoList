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


# class ToDoPostForm(forms.ModelForm):
#     class Meta:
#         model = ToDo
#         fields = ('content',)

class ToDoForm(forms.Form):
    invested_time = forms.DecimalField(max_digits=5, decimal_places=2, default=0.0)

