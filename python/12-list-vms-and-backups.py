import json
import requests

requests.urllib3.disable_warnings()

nbu_api_content_type="application/vnd.netbackup+json;version=5.0;charset=UTF-8"
NBU_API_KEY="A8fmNjyB5DvvzAN1CnRWblMv160U1Vt5hs5P2fqj81pJh9224HRus-w9YuXnwSMa"
nbu_api_hostname="nbumaster.lab.local"
nbu_api_baseurl="https://"+nbu_api_hostname+":1556/netbackup"
asset_id="84ba26e1-bd89-45c6-9ad4-196b0d8f9287"

headers={'Accept': nbu_api_content_type,
         'Authorization': NBU_API_KEY}

#params=dict(
#'page[limit]'='10',
#'page[disable]'='true',
#)

response=requests.get(nbu_api_baseurl+
          "/asset-service/workloads/vmware/assets?page%5Blimit%5D=10&page%5Bdisable%5D=true",
          verify=False,
          headers=headers)

parsed1=response.json()
# print(json.dumps(parsed, indent=4, sort_keys=True))

for idx,item in enumerate(parsed1['data']):
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
print()
print("Listing backups for:")
print("Machine index: ", i)
print("Displayname: ",parsed1['data'][i]['attributes']['commonAssetAttributes']['displayName'])
assted_id=parsed1['data'][i]['id']
print("NBU asset id: ",asset_id)

print()
print("Backups:")
response=requests.get(nbu_api_baseurl+
          "/recovery-point-service/workloads/vmware/recovery-points?page%5Blimit%5D=100&page%5Boffset%5D=0&filter=assetId+eq+%27"+asset_id+"%27+and+%28backupTime+ge+2021-11-01T00%3A00%3A00.000Z%29&include=optionalVmwareRecoveryPointInfo",
          verify=False,
          headers=headers)

parsed2=response.json()

for idx,item in enumerate(parsed2['data']):
        print("Index:", idx)
        print("BackupTime:\t",item['attributes']['backupTime'])
        print("id (referenced by NBU):",item['id'])
        print("JobID:",item['attributes']['extendedAttributes']['imageAttributes']['jobId'])
        print("copyNumber:",item['attributes']['extendedAttributes']['imageAttributes']['fragments'][0]['copyNumber'])
        print("")
