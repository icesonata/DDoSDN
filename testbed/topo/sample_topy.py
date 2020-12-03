from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')

        list_hosts = []
        for h in range(6):
            list_hosts.append(self.addHost('h%s') % (h + 1))

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')

        # Linking
        self.addLink(h1, s4)
        self.addLink(h2, s4)

        self.addLink(h3, s3)
        self.addLink(h4, s3)

        self.addLink(h5, s5)
        self.addLink(h6, s5)

def simpleTest():
    topo = SingleSwitchTopo()
    net = Mininet(topo)
    net.start()
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    simpleTest()