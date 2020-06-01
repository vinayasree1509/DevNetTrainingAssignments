import json
if __name__ == '__main__':
    #open file to read
        raw_json = open('../data/dnac_devices.json').read()
        #parsing the raw data
        parsed_json = json.loads(raw_json)
        for data in parsed_json['response']:
            print('Device Details')
            print('id',data['id'])
            print('type',data['type'])
            print('family',data['family'])
            print('softwareType',data['softwareType'])
            print('managementIpAddress',data['managementIpAddress'],'\n')
            