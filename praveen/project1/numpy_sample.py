import numpy as np
import requests
nums = np.array([1,2,3,4])
print("max num is : {0}".format(np.max(nums)))
res = requests.get('https://w3schools.com/python/demopage.htm')
print(res.text)
