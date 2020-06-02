import requests
import json

def apiRequest(req):
    response = requests.request(req['method'],req['url'],headers=req['headers'],data=req['payload'])
    return response.text.encode('utf8')

if __name__ == '__main__':
        request = {'url' :"https://sandboxdnac2.cisco.com/api/system/v1/auth/token", 'payload': {}, 'headers':{'Authorization': 'Basic ZG5hY2RldjpEM3Y5M1RAd0sh'},'method':'POST'}
        data = json.loads(apiRequest(request))
        request = {'url' :"https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device", 'payload': {}, 'headers':{'x-auth-token':data['Token']},'method':'GET'}
        raw_json = apiRequest(request)
        parsed_json = json.loads(raw_json)
        for data in parsed_json['response']:
            print('Device id',data['id'])
            print('Device type',data['type'])
            print('Device family',data['family'])
            print('Device softwareType',data['softwareType'])
            print('Device managementIpAddress',data['managementIpAddress'],'\n')




