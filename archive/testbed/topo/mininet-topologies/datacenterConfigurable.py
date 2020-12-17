"""
A simple datacenter topology script for Mininet.

    [ s1 ]================================.
      ,---'       |                       |
    [ s1r1 ]=.  [ s1r2 ]=.     ...      [ s1r# ]=.
    [ h1r1 ]-|  [ h1r2 ]-|     ...      [ h1r# ]-|
    [ h2r1 ]-|  [ h2r2 ]-|     ...      [ h2r# ]-|
       ...   |     ...   |     ...         ...   |
    [ h#r1 ]-'  [ h#r2 ]-'     ...      [ h#r# ]-'
"""

from mininet.topo import Topo
from mininet.util import irange

class DatacenterConfigurableTopo( Topo ):
    "Configurable Datacenter Topology"

    def build( self, numRacks=4, numHostsPerRack=4 ):
        self.racks = []
        rootSwitch = self.addSwitch( 's1' )
        for i in irange( 1, numRacks ):
            rack = self.buildRack( i, numHostsPerRack=numHostsPerRack )
            self.racks.append( rack )
            for switch in rack:
                self.addLink( rootSwitch, switch )

    def buildRack( self, loc, numHostsPerRack ):
        "Build a rack of hosts with a top-of-rack switch"

        dpid = ( loc * 16 ) + 1
        switch = self.addSwitch( 's1r%s' % loc, dpid='%x' % dpid )

        for n in irange( 1, numHostsPerRack ):
            host = self.addHost( 'h%sr%s' % ( n, loc ) )
            self.addLink( switch, host )

        # Return list of top-of-rack switches for this rack
        return [switch]

# Allows the file to be imported using `mn --custom <filename> --topo dcconfig`
topos = {
    'dcconfig': DatacenterConfigurableTopo
}
