import re


def cve_match(value: str) -> list:
    """Match all CVE codes in a string, can have up to 7 trailing digits"""
    cve_regex = r'CVE-(?:1999|2\d{3})-\d{4,7}'
    return re.findall(cve_regex, value)
