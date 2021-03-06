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
    s1001 = Node( 's1001', inNamespace=False )
    s1002 = Node( 's1002', inNamespace=False )
    s1003 = Node( 's1003', inNamespace=False )
    s1004 = Node( 's1004', inNamespace=False )

    s2001 = Node( 's2001', inNamespace=False )
    s2002 = Node( 's2002', inNamespace=False )
    s2003 = Node( 's2003', inNamespace=False )
    s2004 = Node( 's2004', inNamespace=False )
    s2005 = Node( 's2005', inNamespace=False )
    s2006 = Node( 's2006', inNamespace=False )
    s2007 = Node( 's2007', inNamespace=False )
    s2008 = Node( 's2008', inNamespace=False )

    s3001 = Node( 's3001', inNamespace=False )
    s3002 = Node( 's3002', inNamespace=False )
    s3003 = Node( 's3003', inNamespace=False )
    s3004 = Node( 's3004', inNamespace=False )
    s3005 = Node( 's3005', inNamespace=False )
    s3006 = Node( 's3006', inNamespace=False )
    s3007 = Node( 's3007', inNamespace=False )
    s3008 = Node( 's3008', inNamespace=False )

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
    Link( h1, s3001 )
    Link( h2, s3001 )
    Link( h3, s3002 )
    Link( h4, s3002 )
    Link( h5, s3003 )
    Link( h6, s3003 )
    Link( h7, s3004 )
    Link( h8, s3004 )
    Link( h9, s3005 )
    Link( h10, s3005 )
    Link( h11, s3006 )
    Link( h12, s3006 )
    Link( h13, s3007 )
    Link( h14, s3007 )
    Link( h15, s3008 )
    Link( h16, s3008 )

    info( "*** Creating Switch-Switch links\n" )
    Link( s1001, s2001 )
    Link( s1001, s2003 )
    Link( s1001, s2005 )
    Link( s1001, s2007 )

    Link( s1002, s2001 )
    Link( s1002, s2003 )
    Link( s1002, s2005 )
    Link( s1002, s2007 )

    Link( s1003, s2002 )
    Link( s1003, s2004 )
    Link( s1003, s2006 )
    Link( s1003, s2008 )

    Link( s1004, s2002 )
    Link( s1004, s2004 )
    Link( s1004, s2006 )
    Link( s1004, s2008 )

    Link( s2001, s3001 )
    Link( s2001, s3002 )
    Link( s2002, s3001 )
    Link( s2002, s3002 )

    Link( s2003, s3003 )
    Link( s2003, s3004 )
    Link( s2004, s3003 )
    Link( s2004, s3004 )

    Link( s2005, s3005 )
    Link( s2005, s3006 )
    Link( s2006, s3005 )
    Link( s2006, s3006 )

    Link( s2007, s3007 )
    Link( s2007, s3008 )
    Link( s2008, s3007 )
    Link( s2008, s3008 )

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
    h16.cmdPrint( 'time iperf -c ' + h1.IP() + ' -t2 -n 100M &')
    h16.cmdPrint( 'ping -c100 ' + h1.IP())

    info( "*** Stopping network\n" )
    controller.cmd( 'kill %' + cname )
    info( '\n' )

if __name__ == '__main__':
    setLogLevel( 'info' )
    info( '*** Scratch network demo (kernel datapath)\n' )
    Mininet.init()
    scratchNet()
