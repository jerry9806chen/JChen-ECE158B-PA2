from mininet.net import Mininet
from mininet.node import Node
from mininet.link import Link
from mininet.log import setLogLevel, info
from mininet.util import quietRun
from mininet.topo import Topo

class TwoHop( Topo ):
    def __init__( self, runTest=False ):
        Topo.__init__(self)
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        h13 = self.addHost('h13')
        h14 = self.addHost('h14')
        h15 = self.addHost('h15')
        h16 = self.addHost('h16')
        s = self.addSwitch('s1')
        self.addLink( h1, s )
        self.addLink( h2, s )
        self.addLink( h3, s )
        self.addLink( h4, s )
        self.addLink( h5, s )
        self.addLink( h6, s )
        self.addLink( h7, s )
        self.addLink( h8, s )
        self.addLink( h9, s )
        self.addLink( h10, s )
        self.addLink( h11, s )
        self.addLink( h12, s )
        self.addLink( h13, s )
        self.addLink( h14, s )
        self.addLink( h15, s )
        self.addLink( h16, s )

        print(h1)

        if runTest:
            h1.cmdPrint( 'iperf -s &')
            h16.cmdPrint( 'ping -c100 ' + h1.IP() )
            h1.cmdPrint( 'time iperf -c ' + h1.IP() + ' -t2 -n 100M')

topos = { 'twohop': ( lambda: TwoHop() ) }

if __name__ == '__main__':
    setLogLevel( 'info' )
    topo = TwoHop(True)
