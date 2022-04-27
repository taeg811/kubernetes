from kubernetes import client, config
import prometheus_client
from prometheus_client import start_http_server
import time
import os
import json


host = 'https://10.73.1.115:8443/api/v1/pods'
c_crt = './client.crt'
c_key = './client.key'

UPDATE_PERIOD = 100
NUM_POD = prometheus_client.Gauge('num_pod', 'Hold current pods number')

if __name__ == '__main__':
    # Start up the server to expose the metrics.
  start_http_server(8088)
    # Generate requests.
while True:
  curl_str = f'curl -k {host} --key {c_key} --cert {c_crt}'
  print(curl_str)
#  zapros = json.loads((os.popen(curl_str)).read())
  zapros = os.popen(curl_str).read() 
#  print(zapros)
  zapros = json.loads(zapros)
  pods = 0
  for data in zapros['items']: pods = pods+1

  NUM_POD.set(pods)
  print(pods)
  time.sleep(UPDATE_PERIOD)















#NUM_POD.labels('NUM_POD').set(sum)
# можно получить    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

