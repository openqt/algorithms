#!/usr/bin/env python
# coding=utf-8
# https://github.com/openshift/origin-metrics/blob/master/docs/hawkular_metrics.adoc
# 得到所有监控数据
import requests, logging, json, sys

logging.basicConfig(level=logging.DEBUG)

headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJ0ZXN0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6InJvYm90LXRva2VuLWZ0cTlxIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6InJvYm90Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiZTE4YmYzNmQtMzE4OC0xMWU4LThkZGYtNzBlMjg0MDU4M2ZjIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OnRlc3Q6cm9ib3QifQ.XVZB2KBgX1hy2XxjkcYIRVchjc4G_wDc9yTj4_KR96fnICUJosGi8hN0Dy0-ZlSplbB7CgDDh2S1EZ8TDcyC4WLIiLsFBtyfY-WKhE8fNVDCbH7yQma2kKeiMzoF7-y8JyvtQSD1JKm2tOcGO4G92xqsAlfityZIiKrkmS2Cn8Br-8y8VjpvT-hHdzM99Zk4f1XH2xTpUjRvZie1_Bj2Ic-L9VzQQZtn-3_5f7VhyhkZeZw7B9RFiLcjOjVj94nYtFv5seW27pURVM8GPcLcgr1AqIXQihiCmDOM_6XLGIz-x244OQzufj4TfRJmnY2K60v5e5ofXtu-BBQbPovr7g",
    "Accept": "application/json",
    "Hawkular-Tenant": "test",
}

resp = requests.get("https://metrics.ibis.cn/hawkular/metrics/metrics", verify=False, headers=headers)
json.dump(resp.json(), sys.stdout, indent=2)
