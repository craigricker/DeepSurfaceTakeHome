import datetime

from challenge1.overlap import overlap
from challenge2.extract_cves import extract_cves

if __name__ == '__main__':
    # Challenge 1
    a = [8, 1, 2, 4, 5, 2, 7, 1, 9, 4, 2]
    b = [7, 4, 2, 3, 0, 6]
    c = [1, 2, 4, 5, 2, 7, 1, 9, 4, 2, 3, 9, 9, 8]
    print('Outputting overlap between provided examples for challenge 1')
    print(overlap([a, b, c]))
    challenge_2_data = [
        {
            'id': 72941762,
            'description': 'Buffer overflow in the Web Client service (WebClnt.dll) for Microsoft Windows XP SP1 and SP2, and Server 2003 up to SP1, allows remote authenticated users or Guests to execute arbitrary code via crafted RPC requests, a different vulnerability than CVE-2005-1207.',
            'relates-to': ['CVE-2005-1106', 'CVE-2005-1206', 'CVE-2015-0020'],
            'rating': 7.8,
            'published': datetime.datetime(2005, 10, 29, 9, 40, 55, 945333)
        },
        {
            'id': 6563719,
            'description': 'Microsoft Internet Explorer 6 through 11 allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption) via a crafted web site, aka "Internet Explorer Memory Corruption Vulnerability," a different vulnerability than CVE-2015-0020, CVE-2015-0022, CVE-2015-0026, CVE-2015-0030, CVE-2015-0031, CVE-2015-0036, and CVE-2015-0041.',
            'relates-to': ['CVE-2015-0020', 'CVE-2015-0036'],
            'rating': 9.8,
            'published': datetime.datetime(2015, 8, 21, 5, 50, 35, 12334)
        },
        {
            'id': 9929220,
            'description': 'An issue was discovered in urllib2 in Python 2.x through 2.7.16 and urllib in Python 3.x through 3.7.3. CRLF injection is possible if the attacker controls a url parameter, as demonstrated by the first argument to urllib.request.urlopen with \\r\\n (specifically in the path component of a URL that lacks a ? character) followed by an HTTP header or a Redis command. This is similar to the CVE-2019-9740 query string issue.',
            'rating': 4.7,
            'relates-to': ['USN-4127-2', 'CVE-2019-9740'],
            'published': datetime.datetime(2019, 4, 21, 1, 30, 11, 17229)
        },
        {
            'id': 54431,
            'description': 'Juniper Networks ScreenOS devices do not pad Ethernet packets with zeros, and thus some packets can contain fragments of system memory or data from previous packets. This issue is often detected as CVE-2003-0001. The issue affects all versions of Juniper Networks ScreenOS prior to 6.3.0r25.',
            'rating': 8.7,
            'relates-to': None,
            'published': datetime.datetime(2018, 1, 1, 1, 31, 41, 33291)
        }
    ]

    # Challenge 2
    challenge_2_results = []
    print('Outputting matched CVE records for challenge 2')
    for item in challenge_2_data:
        challenge_2_results += extract_cves(item)
    print(challenge_2_results)
