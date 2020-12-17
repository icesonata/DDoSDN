#!/usr/bin/env python
"""
Test the example datacenter topologies

Requires `ryu-manager` to be on the PATH. Assumes test is run in the same
directory as the topology definition scripts.

Usage: $ sudo ./datacenterTests.py

Based in part on Mininet's own tests.
"""

import unittest
import sys
sys.path.append('.')
from mininet.net import Mininet
from mininet.node import Ryu, OVSSwitch
from mininet.clean import cleanup

from minimal import MinimalTopo
from datacenterBasic import DatacenterBasicTopo
from datacenterConfigurable import DatacenterConfigurableTopo
from datacenterHARoot import DatacenterHARootTopo
from datacenterHAFull import DatacenterHAFullTopo

# pylint: disable=E1102,E1101

class testSwitchTopo(object):
    "Test ping with the specified topology"
    topoClass = None # Override with topology
    ryuParams = ['ryu.app.simple_switch_13']
    mayDrop = 0

    def controller(self, name, **params):
        return Ryu(name, *self.ryuParams, **params)

    @staticmethod
    def tearDown():
        "Clean up the network"
        if sys.exc_info != (None, None, None):
            cleanup()

    def testPing(self):
        "Create the network and run a ping test"
        net = Mininet(topo=self.topoClass(), controller=self.controller,
                      switch=OVSSwitch, waitConnected=True)
        dropped = net.run(net.ping)
        self.assertLessEqual(dropped, self.mayDrop)


class TestMinimalTopo(testSwitchTopo, unittest.TestCase):
    "Test the minimal topology"
    topoClass = MinimalTopo

class TestDatacenterBasicTopo(testSwitchTopo, unittest.TestCase):
    "Test the basic example datacenter topology"
    topoClass = DatacenterBasicTopo

class TestDatacenterConfigurableTopo(testSwitchTopo, unittest.TestCase):
    "Test the Configurable datacenter topology"
    topoClass = DatacenterConfigurableTopo

class TestDatacenterHARootTopo(testSwitchTopo, unittest.TestCase):
    "Test the HA Root datacenter topology"
    topoClass = DatacenterHARootTopo
    ryuParams = ['ryu.app.simple_switch_stp']
    mayDrop = 15

class TestDatacenterHAFullTopo(testSwitchTopo, unittest.TestCase):
    "Test the basic example datacenter topology"
    topoClass = DatacenterHAFullTopo
    ryuParams = ['ryu.app.simple_switch_stp']
    mayDrop = 15

if __name__ == '__main__':
    unittest.main()
