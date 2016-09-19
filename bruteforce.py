#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

lst = list(itertools.product([0, 1], repeat=64))
print lst