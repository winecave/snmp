# -*- coding: utf-8 -*-
#
# created: 2018.01.10
# author : k.inokuchi
#

import common as com
from pysnmp.hlapi import *

OID = 'sysUpTime'
COMMUNITY_NAME = 'github'
TARGET = '192.168.0.20'

varBinds = getCmd(
           SnmpEngine(),
           CommunityData(COMMUNITY_NAME, mpModel=0),
           UdpTransportTarget((TARGET, 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', OID, 0)))
print(next(varBinds))
print('-'*50)
print(next(varBinds, 'no more item'))
