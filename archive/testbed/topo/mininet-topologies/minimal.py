#!/usr/bin/python

"""
A simple minimal topology script for Mininet.

Based in part on examples in the [Introduction to Mininet] page on the Mininet's
project wiki.

[Introduction to Mininet]: https://github.com/mininet/mininet/wiki/Introduction-to-Mininet#apilevels

"""

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSSwitch

class MinimalTopo( Topo ):
    "Minimal topology with a single switch and two hosts"

    def build( self ):
        # Create two hosts.
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )

        # Create a switch
        s1 = self.addSwitch( 's1' )

        # Add links between the switch and each host
        self.addLink( s1, h1 )
        self.addLink( s1, h2 )

def runMinimalTopo():
    "Bootstrap a Mininet network using the Minimal Topology"

    # Create an instance of our topology
    topo = MinimalTopo()

    # Create a network based on the topology using OVS and controlled by
    # a remote controller.
    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController( name, ip='127.0.0.1' ),
        switch=OVSSwitch,
        autoSetMacs=True )

    # Actually start the network
    net.start()

    # Drop the user in to a CLI so user can run commands.
    CLI( net )

    # After the user exits the CLI, shutdown the network.
    net.stop()

if __name__ == '__main__':
    # This runs if this file is executed directly
    setLogLevel( 'info' )
    runMinimalTopo()

# Allows the file to be imported using `mn --custom <filename> --topo minimal`
topos = {
    'minimal': MinimalTopo
}
