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
    s1 = Node( 's1', inNamespace=False )
    s2 = Node( 's2', inNamespace=False )
    s3 = Node( 's3', inNamespace=False )
    s4 = Node( 's4', inNamespace=False )
    s5 = Node( 's5', inNamespace=False )
    s6 = Node( 's6', inNamespace=False )
    s7 = Node( 's7', inNamespace=False )
    s8 = Node( 's8', inNamespace=False )
    s9 = Node( 's9', inNamespace=False )
    s10 = Node( 's10', inNamespace=False )
    s11 = Node( 's11', inNamespace=False )
    s12 = Node( 's12', inNamespace=False )
    s13 = Node( 's13', inNamespace=False )
    s14 = Node( 's14', inNamespace=False )
    s15 = Node( 's15', inNamespace=False )
    s16 = Node( 's16', inNamespace=False )

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

    info( "*** Creating Host-Switch links\n" )
    Link( h1, s1 )
    Link( h2, s2 )
    Link( h3, s3 )
    Link( h4, s4 )
    Link( h5, s5 )
    Link( h6, s6 )
    Link( h7, s7 )
    Link( h8, s8 )
    Link( h9, s9 )
    Link( h10, s10 )
    Link( h11, s11 )
    Link( h12, s12 )
    Link( h13, s13 )
    Link( h14, s14 )
    Link( h15, s15 )
    Link( h16, s16 )

    info( "*** Creating Switch-Switch links\n" )
    Link( s1, s2 )
    Link( s2, s3 )
    Link( s3, s4 )
    Link( s4, s5 )
    Link( s5, s6 )
    Link( s6, s7 )
    Link( s7, s8 )
    Link( s8, s9 )
    Link( s9, s10 )
    Link( s10, s11 )
    Link( s11, s12 )
    Link( s12, s13 )
    Link( s13, s14 )
    Link( s14, s15 )
    Link( s15, s16 )

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

    info( "*** Running test\n" )
    h1.cmdPrint( 'iperf -s &')
    #h16.cmdPrint( 'ping -c100 ' + h1.IP() + ' &')# + ' time iperf -c ' + h1.IP() + ' -t2 -n 100M')
    #h1.cmdPrint( 'iperf -s &')
    h16.cmdPrint( 'time iperf -c ' + h1.IP() + ' -t2 -n 100M &')
    h16.cmdPrint( 'ping -c100 ' + h1.IP())# + ' time iperf -c ' + h1.IP() + ' -t2 -n 100M')

    info( "*** Stopping network\n" )
    controller.cmd( 'kill %' + cname )
    info( '\n' )

if __name__ == '__main__':
    setLogLevel( 'info' )
    info( '*** Scratch network demo (kernel datapath)\n' )
    Mininet.init()
    scratchNet()
