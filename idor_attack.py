import requests

for i in range(1,5001):
    l=f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    re=requests.get(l)

    if re.status_code == 200:
        print(l)