from mininet.net import Mininet
from mininet.node import Node
from mininet.link import Link
from mininet.log import setLogLevel, info
from mininet.util import quietRun

from time import sleep

def scratchNet( cname='controller', cargs='-v ptcp:' ):
    "Create network from scratch using Open vSwitch."

    info( "*** Creating nodes\n" )
    controller = Node( 'c0', inNamespace=False )
    switch = Node( 's0', inNamespace=False )
    h1 = Node( 'h1' )
    h2 = Node( 'h2' )
    h3 = Node( 'h3' )
    h4 = Node( 'h4' )
    h5 = Node( 'h5' )
    h6 = Node( 'h6' )
    h7 = Node( 'h7' )
    h8 = Node( 'h8' )
    h9 = Node( 'h9' )
    h10 = Node( 'h10' )
    h11 = Node( 'h11' )
    h12 = Node( 'h12' )
    h13 = Node( 'h13' )
    h14 = Node( 'h14' )
    h15 = Node( 'h15' )
    h16 = Node( 'h16' )

    info( "*** Creating links\n" )
    Link( h1, switch )
    Link( h2, switch )
    Link( h3, switch )
    Link( h4, switch )
    Link( h5, switch )
    Link( h6, switch )
    Link( h7, switch )
    Link( h8, switch )
    Link( h9, switch )
    Link( h10, switch )
    Link( h11, switch )
    Link( h12, switch )
    Link( h13, switch )
    Link( h14, switch )
    Link( h15, switch )
    Link( h16, switch )

    info( "*** Configuring hosts\n" )
    h1.setIP( '192.168.123.1/24' )
    h2.setIP( '192.168.123.2/24' )
    h3.setIP( '192.168.123.3/24' )
    h4.setIP( '192.168.123.4/24' )
    h5.setIP( '192.168.123.5/24' )
    h6.setIP( '192.168.123.6/24' )
    h7.setIP( '192.168.123.7/24' )
    h8.setIP( '192.168.123.8/24' )
    h9.setIP( '192.168.123.9/24' )
    h10.setIP( '192.168.123.10/24' )
    h11.setIP( '192.168.123.11/24' )
    h12.setIP( '192.168.123.12/24' )
    h13.setIP( '192.168.123.13/24' )
    h14.setIP( '192.168.123.14/24' )
    h15.setIP( '192.168.123.15/24' )
    h16.setIP( '192.168.123.16/24' )
    info( str( h1 ) + '\n' )
    info( str( h2 ) + '\n' )
    info( str( h3 ) + '\n' )
    info( str( h4 ) + '\n' )
    info( str( h5 ) + '\n' )
    info( str( h6 ) + '\n' )
    info( str( h7 ) + '\n' )
    info( str( h8 ) + '\n' )
    info( str( h9 ) + '\n' )
    info( str( h10 ) + '\n' )
    info( str( h11 ) + '\n' )
    info( str( h12 ) + '\n' )
    info( str( h13 ) + '\n' )
    info( str( h14 ) + '\n' )
    info( str( h15 ) + '\n' )
    info( str( h16 ) + '\n' )

    info( "*** Starting network using Open vSwitch\n" )
    controller.cmd( cname + ' ' + cargs + '&' )
    switch.cmd( 'ovs-vsctl del-br dp0' )
    switch.cmd( 'ovs-vsctl add-br dp0' )
    for intf in switch.intfs.values():
        switch.cmd( 'ovs-vsctl add-port dp0 %s\n' % intf )

    # Note: controller and switch are in root namespace, and we
    # can connect via loopback interface
    switch.cmd( 'ovs-vsctl set-controller dp0 tcp:127.0.0.1:6633' )

    info( '*** Waiting for switch to connect to controller' )
    while 'is_connected' not in quietRun( 'ovs-vsctl show' ):
        sleep( 1 )
        info( '.' )
    info( '\n' )

    info( "*** Running test\n" )
    h16.cmdPrint( 'ping -c1 ' + h1.IP() )
    h1.cmdPrint( 'iperf -s &')
    h1.cmdPrint( 'time iperf -c ' + h1.IP() + ' -t2 -n 100M')

    info( "*** Stopping network\n" )
    controller.cmd( 'kill %' + cname )
    switch.cmd( 'ovs-vsctl del-br dp0' )
    switch.deleteIntfs()
    info( '\n' )

if __name__ == '__main__':
    setLogLevel( 'info' )
    info( '*** Scratch network demo (kernel datapath)\n' )
    Mininet.init()
    scratchNet()
