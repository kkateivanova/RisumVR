from zmq_tools import *


ctx = zmq.Context()
requester = ctx.socket(zmq.REQ)
requester.connect('tcp://localhost:54095')

requester.send('SUB_PORT')
ipc_sub_port = requester.recv()
monitor = Msg_Receiver(ctx,'tcp://localhost:%s'%ipc_sub_port,topics=('logging.',))

while True:
    topic,l = monitor.recv()
    print '%s: %s - %s'%(l['name'],l['levelname'],l['msg'])
