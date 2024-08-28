import yaml

with open('vmlist.yml', 'r') as file:
    vmdata = yaml.safe_load_all(file)
    
    for data in vmdata:
        for resource in data['resources']:
            print("************")
            #print(resource['spec']['template'])
            print("VM: " + resource['metadata']['name'])
            #print(resource['metadata']['name'])
            #print(resource['spec']['template']['spec']['domain'])
            print("CORES: ",resource['spec']['template']['spec']['domain']['cpu']['cores'])
            #print(resource['spec']['template']['spec']['domain']['cpu']['cores'])


            print("---------")
