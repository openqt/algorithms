import zerorpc


class Hello(object):
    def hi(self, name):
        print("Hi, %s" % name)
        zerorpc.gevent.sleep(1)
        print("- %s -" % name)


s = zerorpc.Server(Hello())
s.bind("inproc://tt")
zerorpc.gevent.spawn(s.run)

client = zerorpc.Client("inproc://tt")
for i in range(10):
    print(client.hi("Whl-%d" % i, async=True))

zerorpc.gevent.sleep(3)
print('END')
