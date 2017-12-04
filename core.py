#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
  Author: Lynch
"""
from __future__ import absolute_import

from utils import *
import pandas as pd
import numpy as np
import numbers as nb

class CHECK_x(object):
    """
    
    """

    def __init__(self,x):
        self.x = x
    def __CHECK_str(self):
        pass
    def __CHECK_num(self):
        pass
    def __CHECK_continus(self):
        pass
    def __CHECK_discrete(self):
        pass
    def __CHECK_nan(self):
        pass

    def CHECK_(self):
        if self.__CHECK_str():
            pass
        if self.__CHECK_num():
            pass
        if self.__CHECK_continus():
            pass
        if self.__CHECK_discrete():
            pass
        if self.__CHECK_nan():
            pass


class DCore(CHECK_x):
    """
    
    """

    def __init__(self,x):
        super(DCore,self).__init__(x)
        self.value = x
        self.type = None
        self.stats = None
        self.set = None
        self.names = None

    def f_names(self):
        """
        
        :return: 
        """
        self.names = list(self.value.columns)

    def f_type(self):
        """
        
        :return: 
        """
        self.type = self.CHECK_()


    def f_set(self):
        """
        
        :return: 
        """

        pass

    def f_stats(self):
        """
        
        :return: 
        """
        pass


