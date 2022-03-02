from challenge2.cve_match import cve_match


def extract_cves(input_data) -> list:
    '''
    Recursive approach for extracting
    :param input_data:
    :return:
    '''
    mentioned_cves = []
    if isinstance(input_data, dict):
        for value in input_data.values():
            mentioned_cves += extract_cves(value)
        return mentioned_cves
    elif isinstance(input_data, list):
        for sub_value in input_data:
            mentioned_cves += cve_match(sub_value)
        return mentioned_cves
    elif isinstance(input_data, str):
        return cve_match(input_data)
    else:
        return mentioned_cves
