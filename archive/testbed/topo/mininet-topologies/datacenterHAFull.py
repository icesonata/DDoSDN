"""
A simple datacenter topology script for Mininet.

      ,----------------------------.     Each root switch connected in ring.
    [ s1 ]------[ s2 ]--- ... ---[ s# ]
      |           |                |     Each ToR switch connects to its
  ,==='==========='================'     associated root switch. (s3r1 <-> s3)
  |-[ s1r1 ]=.  [ s1r2 ]=.     ...      [ s1r# ]=.
  |-[ s2r1 ]=|  [ s2r2 ]=|     ...      [ s2r# ]=|
  |    ...   |     ...   |     ...         ...   |
  `-[ s#r1 ]=|  [ s#r2 ]=|     ...      [ s#r# ]=|
             |           |                       |
    [ h1r1 ]-|  [ h1r2 ]-|     ...      [ h1r# ]-|
    [ h2r1 ]-|  [ h2r2 ]-|     ...      [ h2r# ]-|
       ...   |     ...   |     ...         ...   |
    [ h#r1 ]-'  [ h#r2 ]-'     ...      [ h#r# ]-'
"""

from mininet.topo import Topo
from mininet.util import irange

class DatacenterHAFullTopo( Topo ):
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
            rack = self.buildRack( i, numHostsPerRack=numHostsPerRack,
                                   numHASwitches=numHASwitches )
            self.racks.append( rack )

            # For every HA switch, add a link between the rack switch and root
            # switch of the same ID
            for j in range( numHASwitches ):
                self.addLink( rootSwitches[j], rack[j] )

    def buildRack( self, loc, numHostsPerRack, numHASwitches ):
        "Build a rack of hosts with a top-of-rack switch"

        switches = []
        for n in irange( 1, numHASwitches ):
            # Make sure each switch gets a unique DPID based on the location
            # in the rack for easy decoding when looking at logs.
            dpid = ( loc * 16 ) + n
            switch = self.addSwitch( 's%sr%s' % (n, loc), dpid='%x' % dpid )
            switches.append( switch )

        for n in irange( 1, numHostsPerRack ):
            host = self.addHost( 'h%sr%s' % ( n, loc ) )

            # Add a link from every top-of-rack switch to the host
            for switch in switches:
                self.addLink( switch, host )

        # Return list of top-of-rack switches for this rack
        return switches

# Allows the file to be imported using `mn --custom <filename> --topo dafull`
topos = {
    'dchafull': DatacenterHAFullTopo
}
