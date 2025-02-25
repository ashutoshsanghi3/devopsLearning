import boto3
def create_ec2_instance():
    try:
        print("creating ec2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId = "ami-085ad6ae776d8f09c",
            MaxCount = 1,
            MinCount = 1,
            InstanceType = "t2.micro",
            KeyName = "first_instance"
        )
    except Exception as e:
        print(e)

create_ec2_instance()