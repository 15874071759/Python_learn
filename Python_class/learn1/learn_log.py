#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-04 11:47 
# @Author : huff 
# @File : learn_log.py 
# @Software: PyCharm

import logging,time

lognow = time.strftime("%Y%m%d_%H:%M:%S", time.localtime(time.time()))
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s--->%(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='../log/log_'+lognow+'.log',
                    filemode='w')
logging.debug("debug info")
logging.info("info info")
logging.warning("warning info")
logging.error("error info")

