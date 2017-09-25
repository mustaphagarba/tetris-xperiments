#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import pygame

from pygame.locals import *

def main():
    pygame.init()
    pygame.display.set_mode((400, 500))

    while True:
        for event in pygame.event.get_event():
            if event.type == QUIT:
                terminate()

if __name__ == '__main__':
    main()
