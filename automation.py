import boto3
#import paramiko

ec2 = boto3.client('ec2', aws_access_key_id='AKIAUJRYN7IHEN7ESBWK', aws_secret_access_key='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', region_name='us-east-1')
# instance_params = {
#         'ImageId': 'ami-0e13fb78f793e43a4'  # 'ami-0c7217cdde317cfec' Specify the AMI ID for your desired operating system
#         'InstanceType': 't3.micro',          # Specify the instance type
#         'KeyName': 'Shree',     # Specify the key pair name for SSH access
#         'MinCount': 1,
#         'MaxCount': 1
#     }

user_data_script = f"""#!bin/bash
exec > /tmp/user-data.log 2>&1
sudo apt-get update -y
sudo apt-get install nginx -y
sudo curl -sL https://deb.nodesource.com/setup_current.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt install npm
sleep 30
sudo git clone https://writer123456:hkjhkjl123@github.com/writer123456/TravelMemory
sleep 30
sudo touch TravelMemory/backend/.env|sudo chmod 777 TravelMemory/backend/.env
sudo echo "MONGO_URI='mongodb+srv://shree:shree@cluster0.whnkc0r.mongodb.net/'" > TravelMemory/backend/.env
sudo echo "PORT = 3000" >> TravelMemory/backend/.env
cd TravelMemory/backend
pwd > cur_dir.txt

# sudo chmod 755 TravelMemory/backend
# 
# "MONGO_URI=\'mongodb+srv://shree:shree@cluster0.whnkc0r.mongodb.net/'"
# PORT=3000
"""

response = ec2.run_instances(
    ImageId='ami-0c7217cdde317cfec',
    InstanceType='t3.micro',
    KeyName='New_Shree',
    SecurityGroupIds=['sg-0672b0adce594e817'],
    SubnetId='subnet-070f6751946cf9645',
    UserData=user_data_script,
    MinCount=1,
    MaxCount=1
)
print("Instance created:", response['Instances'][0]['InstanceId'])
# describe_instances_response = ec2.describe_instances(InstanceIds=['i-02b0ae10f6951bf5e'])

# print(describe_instances_response['Reservations'][0]['Instances'][0])

