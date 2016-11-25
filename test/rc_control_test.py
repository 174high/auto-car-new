__author__ = 'zhengwang'

import serial
import socket
import time
import pygame
from pygame.locals import *


class RCTest(object):

    def __init__(self):
        print "RCTest init -----"
        pygame.init()
        scrteen=pygame.display.set_mode((640, 480), 0, 32)
        #self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.send_inst = True
        #self.ser.write(chr(5))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('192.168.3.102', 8000))
        self.connection = self.client_socket.makefile('wb')
        self.steer()
 

    def steer(self):
   
        print "----steer--in"
        while self.send_inst:
            for event in pygame.event.get():
                print "--get key event--"
                if event.type == KEYDOWN:
                    key_input = pygame.key.get_pressed()
        
                    # complex orders
                    if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
                        print "Forward Right"
                        self.connection.write(chr(6))
                        self.connection.flush()                                                      

                     # self.ser.write(chr(6))

                    elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
                        print "Forward Left"
                        self.connection.write(chr(7))
                        self.connection.flush()
                       # self.ser.write(chr(7))

                    elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
                        print "Reverse Right"
                        self.connection.write(chr(8))
                        self.connection.flush()
                       #self.ser.write(chr(8))

                    elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
                        print "Reverse Left"
                        self.connection.write(chr(9))
                        self.connection.flush()
                        #self.ser.write(chr(9))

                    # simple orders
                    elif key_input[pygame.K_UP]:
                        print "Forward"
        		self.connection.write(chr(1))
                        self.connection.flush()
                        #self.ser.write(chr(1))

                    elif key_input[pygame.K_DOWN]:
                        print "Reverse"
        		self.connection.write(chr(2))
                        self.connection.flush()
                        #self.ser.write(chr(2))

                    elif key_input[pygame.K_RIGHT]:
                        print "Right"
        		self.connection.write(chr(3))
                        self.connection.flush()
                        #self.ser.write(chr(3))

                    elif key_input[pygame.K_LEFT]:
                        print "Left"
        		self.connection.write(chr(4))
                        self.connection.flush()
                        #self.ser.write(chr(4))

                    # exit
                    elif key_input[pygame.K_x] or key_input[pygame.K_q]:
                        print 'Exit'
        		self.connection.write(chr(0))
                        self.connection.flush()
                        self.send_inst = False
                        #self.ser.write(chr(0))
                        #self.ser.close()
                        break

                elif event.type == pygame.KEYUP:
                    self.connection.write(chr(0))
                    self.connection.flush()
                    #self.ser.write(chr(0))
                 

if __name__ == '__main__':
    RCTest()
