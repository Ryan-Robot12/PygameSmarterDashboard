from typing import Any

from networktables import *

ip = "roborio-4829-frc.local"
NetworkTables.initialize(server=ip)

smartDashboard = NetworkTables.getTable("SmartDashboard")


def getTable(name: str):
    return NetworkTables.getTable(name)


def getValue(nt: NetworkTable = smartDashboard, name: str = "", defaultValue=-1):
    if nt.containsKey(name):
        return nt.getValue(name, defaultValue)
    else:
        return defaultValue


def putValue(nt: NetworkTable = smartDashboard, name: str = "", value=-1):
    nt.putValue(name, value)
