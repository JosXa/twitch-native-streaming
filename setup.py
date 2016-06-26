#!/usr/bin/env python

from setuptools import setup

setup(name='twitch',
      version='1.0',
      description='Twitch Native Streaming',
      author='Joscha Götzer',
      author_email='joscha.goetzer@gmail.com',
      url='http://github.com/Rostgnom/twitch-native-streaming',
      scripts=['twitch/twitch.py'],
      packages=['twitch'],

      # Executable
      entry_points={
          'console_scripts': [
              'twitch = twitch:main',
          ],
      },
      )
