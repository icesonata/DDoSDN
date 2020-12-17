"""
A simple datacenter topology script for Mininet.

    [ s1 ]================================.
      ,---'       |           |           |
    [ s1r1 ]=.  [ s1r2 ]=.  [ s1r3 ]=.  [ s1r4 ]=.
    [ h1r1 ]-|  [ h1r2 ]-|  [ h1r3 ]-|  [ h1r4 ]-|
    [ h2r1 ]-|  [ h2r2 ]-|  [ h2r3 ]-|  [ h2r4 ]-|
    [ h3r1 ]-|  [ h3r2 ]-|  [ h3r3 ]-|  [ h3r4 ]-|
    [ h4r1 ]-'  [ h4r2 ]-'  [ h4r3 ]-'  [ h4r4 ]-'
"""

from mininet.topo import Topo
from mininet.util import irange

class DatacenterBasicTopo( Topo ):
    "Datacenter topology with 4 hosts per rack, 4 racks, and a root switch"

    def build( self ):
        self.racks = []
        rootSwitch = self.addSwitch( 's1' )
        for i in irange( 1, 4 ):
            rack = self.buildRack( i )
            self.racks.append( rack )
            for switch in rack:
                self.addLink( rootSwitch, switch )

    def buildRack( self, loc ):
        "Build a rack of hosts with a top-of-rack switch"

        dpid = ( loc * 16 ) + 1
        switch = self.addSwitch( 's1r%s' % loc, dpid='%x' % dpid )

        for n in irange( 1, 4 ):
            host = self.addHost( 'h%sr%s' % ( n, loc ) )
            self.addLink( switch, host )

        # Return list of top-of-rack switches for this rack
        return [switch]

# Allows the file to be imported using `mn --custom <filename> --topo dcbasic`
topos = {
    'dcbasic': DatacenterBasicTopo
}
