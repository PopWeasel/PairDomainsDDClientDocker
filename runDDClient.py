import argparse
from os import path, chmod
from subprocess import call, CalledProcessError
import sys

EXECUTABLE = "ddclient"

def parseArguments(sysArgs):
    parser = argparse.ArgumentParser(description='Run ddclient')
    parser.add_argument("-u", "--use",
                        metavar="use value",
                        default="web, web=https://myip.pairdomains.com/, web-skip=\"IP Address:\"",
                        help="value for use setting in ddclient config")
    parser.add_argument("-s", "--server",
                        metavar="server value",
                        default="dynamic.pairdomains.com",
                        help="value for server setting in ddclient config")
    parser.add_argument("-l", "--login",
                        metavar="login value",
                        default="pairdomains",
                        help="value for login setting in ddclient config")
    parser.add_argument("-p", "--password",
                        metavar="password value",
                        required=True,
                        help="value for password setting in ddclient config")
    parser.add_argument("-d", "--dns",
                        metavar="domain",
                        required=True,
                        help="domain to update with ddclient")
    parser.add_argument("-o", "--output",
                        metavar="location of ddclient config",
                        default="ddclient.conf",
                        help="path location for ddclient config")
    args = parser.parse_args(sysArgs)
    return args

def writeFile(use, server, login, password, dns, output):
    print("Writing: {}".format(output))
    with open(output, "w") as file:
        file.write("# Config file for ddclient\n");
        file.write("daemon=60 # check every 300 seconds\n");
        file.write("syslog=yes # log update msgs to syslog\n");
        file.write("pid=/var/run/ddclient.pid\n");
        file.write("ssl=yes\n");
        file.write("protocol=dyndns2\n");
        file.write("use={}\n".format(use));
        file.write("server={}\n".format(server));
        file.write("login={}\n".format(login));
        file.write("password={}\n".format(password));
        file.write("{}\n".format(dns));
        chmod(output, 0o300)

def runDDClient(output):
    try:
        call(["{}".format(EXECUTABLE), "-daemon", "120", "-file", "{}".format(output)], shell=False)
    except CalledProcessError as e:
        print("{} ".format(e.cmd()))


if __name__ == '__main__':
    args = parseArguments(sys.argv[1:])
    writeFile(**vars(args))
    runDDClient(args.output)
