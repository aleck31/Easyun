import boto3

def getEC2():
    ec2=boto3.client('ec2')
    """ :type : pyboto3.ec2 """
    instance=ec2.describe_instances()
    print(instance)

if __name__ == '__main__':
    getEC2()