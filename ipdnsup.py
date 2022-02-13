import socket

import dns
import dns.resolver

addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('yahoo.com')

# print(addr1, addr2)


def get_ips_by_dns_lookup(target, port=None):
    '''
        this function takes the passed target and optional port and does a dns
        lookup. it returns the ips that it finds to the caller.

        :param target:  the URI that you'd like to get the ip address(es) for
        :type target:   string
        :param port:    which port do you want to do the lookup against?
        :type port:     integer
        :returns ips:   all of the discovered ips for the target
        :rtype ips:     list of strings

    '''

    if not port:
        port = 443

    return list(map(lambda x: x[4][0], socket.getaddrinfo('{}.'.format(target),port,type=socket.SOCK_STREAM)))

ips = get_ips_by_dns_lookup(target='twitter.com')
# print(ips)


# A RECORD
result = dns.resolver.resolve('hashnode.com', 'A')
A_records = []
for IPval in result:
    A_records.append(IPval.to_text())
# print(A_records)


# CNAME
result = dns.resolver.resolve('mail.hashnode.com', 'CNAME')
for cnameval in result:
    pass
    # print('cname target address:', cnameval.target)

# MX RECORD
result = dns.resolver.resolve('hashnode.com', 'MX')
for exdata in result:
    print('MX Record: ',exdata)
