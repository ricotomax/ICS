#!/usr/bin/env python
'''
Asynchronous Modbus Server Built in Python using the pyModbus module
'''
# Import the libraries we need
from pymodbus.server.async import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
# Create a datastore and populate it with test data
store = ModbusSlaveContext(
di = ModbusSequentialDataBlock(0, [17]*100), # Discrete Inputs
initializer
co = ModbusSequentialDataBlock(0, [17]*100), # Coils initializer
hr = ModbusSequentialDataBlock(0, [17]*100), # Holding Register
initializer
ir = ModbusSequentialDataBlock(0, [17]*100)) # Input Registers
initializer
context = ModbusServerContext(slaves=store, single=True)
# Populate the Modbus server information fields, these get returned as
# response to identity queries
identity = ModbusDeviceIdentification()
identity.VendorName = 'PyModbus Inc.'
identity.ProductCode = 'PM'
identity.VendorUrl = 'https://github.com/riptideio/pyModbus'
identity.ProductName = 'Modbus Server'
identity.ModelName = 'PyModbus'
identity.MajorMinorRevision = '1.0'
# Start the listening server
print "Starting Modbus server..."
StartTcpServer(context, identity=identity, address=("0.0.0.0", 502))