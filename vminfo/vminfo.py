import yaml

with open('vmlist.yml', 'r') as file:
    vmdata = yaml.safe_load_all(file)
    print("VMNAME , CORES , MEMORY") 
    for data in vmdata:
        for resource in data['resources']:
            if("memory" in resource['spec']['template']['spec']['domain']):
                print(resource['metadata']['name'],",",resource['spec']['template']['spec']['domain']['cpu']['cores'],",",resource['spec']['template']['spec']['domain']['memory']['guest'])
            if("requests" in resource['spec']['template']['spec']['domain']['resources']):
                print(resource['metadata']['name'],",",resource['spec']['template']['spec']['domain']['cpu']['cores'],",",resource['spec']['template']['spec']['domain']['resources']['requests']['memory'])
