#!/usr/bin/python
# -*- coding: utf-8 -*-
import mimes

#main is needed on windows
if __name__ == '__main__':
	data = mimes.DM3lib.DM3("sample.dm3", dims=3)
	data.saveh5("test.h5")



