######################### Disclaimer #######################
# Actually I have coded this programme in Kali-Linux
# So,To run this programme accurately: type this in kali-Linux command prompt
# ./<this_file_name.py> -H <target ip address> -p <comma separated ports or a single port>


from socket import *
import optparse
from threading import *


def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print("[+] %d/tcp is Open", tgtPort)
    except:
        print("[-] %d/tcp is Closed", tgtPort)
    finally:
        sock.close()


def portScan(tgtHost, tgtPorts):
    # tgtName = None;
    try:
        tgtIp = gethostbyname(tgtHost)
    # except:
    #     print("[-] Can't Resolve Target Host Ip Address of %s" % tgtHost)
    # try:
        tgtName = gethostbyaddr(tgtIp)
        print('[+] Scan Result for target : ' + tgtName[0])
    except:
        print("[-] Scanned Error for " + tgtIp + "\n    This Error occured due to direct inputed ip address")
    setdefaulttimeout(3)
    for tgtPort in tgtPorts:
        thread = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        thread.start()


def main():
    parser = optparse.OptionParser('Usage of Programme: ' + '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='Specify Target Host')
    parser.add_option('-p', dest='tgtPort', type='string', help='Specify Target Ports separated by comma')
    (options, args) = parser.parse_args()
    target_Host = options.tgtHost
    target_Ports = str(options.tgtPort).split(',')

    if (target_Host == None or target_Ports[0] == None):
        print(parser.usage)
        exit(0);
    portScan(target_Host, target_Ports)


if __name__ == '__main__':
    main()
