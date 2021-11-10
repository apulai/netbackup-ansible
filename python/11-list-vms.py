import json
import requests

requests.urllib3.disable_warnings()

nbu_api_content_type="application/vnd.netbackup+json;version=5.0;charset=UTF-8"
NBU_API_KEY="A8fmNjyB5DvvzAN1CnRWblMv160U1Vt5hs5P2fqj81pJh9224HRus-w9YuXnwSMa"
nbu_api_hostname="nbumaster.lab.local"
nbu_api_baseurl="https://"+nbu_api_hostname+":1556/netbackup"
#asset_id="84ba26e1-bd89-45c6-9ad4-196b0d8f9287"

headers={'Accept': nbu_api_content_type,
         'Authorization': NBU_API_KEY}

#          "/asset-service/workloads/vmware/assets?page%5Blimit%5D=10&page%5Bdisable%5D=true",
#      ?page%5Blimit%5D=10&page%5Bdisable%5D=true",
params={
 'page': {
  'limit': 10,
  'disable': 'true'
 }
}

print("Query start...")
response=requests.get(nbu_api_baseurl+

          "/asset-service/workloads/vmware/assets",
          params = params,
          verify=False,
          headers=headers)
print(response.status_code)
parsed=response.json()
# print(json.dumps(parsed, indent=4, sort_keys=True))

for idx,item in enumerate(parsed['data']):
    if( item['attributes']['assetType'] == 'vm' ):
        print("Index:", idx)
        print("Displayname:\t",item['attributes']['commonAssetAttributes']['displayName'])
        print("id (referenced by NBU):",item['id'])
        print("instanceUuid:",item['attributes']['instanceUuid'])
        print("assetType:",item['attributes']['assetType'])
        print("vCenter:",item['attributes']['vCenter'])
        print("vmAbsolutePath:",item['attributes']['vmAbsolutePath'])
        print("lastDiscoveredTime:",item['attributes']['commonAssetAttributes']['detection']['lastDiscoveredTime'])
        print("nicIpAddresses:",item['attributes']['nicIpAddresses'])
        print("")


i = int(input("Please enter the idx of the VM: "))
print("Machine index: ",i)
print("Displayname:", parsed['data'][i]['attributes']['commonAssetAttributes']['displayName'])
