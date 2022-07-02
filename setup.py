#!/usr/bin/python
# -*- coding: utf-8 -*-
from distutils.core import setup

PLUGIN_DIR = 'Extensions.RaedQuickSignal'

setup(name='enigma2-plugin-extensions-RaedQuickSignal',
       version='1.0',
       author='RAED',
       author_email='rrrr53@hotmail.com',
       description='plugin to show information for channels such as (SNR, AGC, picon, encrypted channel info and also to download picons ).',
       packages=[PLUGIN_DIR],
       package_dir={PLUGIN_DIR: 'usr'},
       package_data={PLUGIN_DIR: ['plugin.png', '*/*.png']},
      )
