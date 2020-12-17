"""
A simple datacenter topology script for Mininet.

      ,----------------------------.     Each root switch connected in ring.
    [ s1 ]------[ s2 ]--- ... ---[ s# ]
      |,----------'                |     Each ToR switch connects to every
      ||,--------------------------'     root switch.
    [ s1r1 ]=.  [ s1r2 ]=.     ...      [ s1r# ]=.
    [ h1r1 ]-|  [ h1r2 ]-|     ...      [ h1r# ]-|
    [ h2r1 ]-|  [ h2r2 ]-|     ...      [ h2r# ]-|
       ...   |     ...   |     ...         ...   |
    [ h#r1 ]-'  [ h#r2 ]-'     ...      [ h#r# ]-'
"""

from mininet.topo import Topo
from mininet.util import irange

class DatacenterHARootTopo( Topo ):
    "Configurable Datacenter Topology"

    def build( self, numRacks=4, numHostsPerRack=4, numHASwitches=2 ):
        # This configuration only supports 15 or less root switches
        if numHASwitches >= 16:
            raise Exception( "Please use less than 16 HA switches" )

        self.racks = []
        rootSwitches = []
        lastRootSwitch = None

        # Create and link all the root switches
        for i in irange( 1, numHASwitches ):
            rootSwitch = self.addSwitch( 's%s' % i )
            rootSwitches.append( rootSwitch )

            # If we have initialized at least two switches, make sure to
            # connect them. This handles s1 -> s2 -> ... -> sN
            if lastRootSwitch:
                self.addLink( lastRootSwitch, rootSwitch )

            lastRootSwitch = rootSwitch

        # Make the final link from the last switch to the first switch
        if numHASwitches > 1:
            self.addLink( lastRootSwitch, rootSwitches[0] )

        for i in irange( 1, numRacks ):
            rack = self.buildRack( i, numHostsPerRack=numHostsPerRack )
            self.racks.append( rack )
            for switch in rack:
                for rootSwitch in rootSwitches:
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

# Allows the file to be imported using `mn --custom <filename> --topo dcharoot`
topos = {
    'dcharoot': DatacenterHARootTopo
}
