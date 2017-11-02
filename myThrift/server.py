import sys, glob  
sys.path.append("gen-py")
from myThrift import HelloService  
from myThrift.ttypes import *  
from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.server import TServer  
import traceback
  
class HelloServiceHandler:  
  def __init__(self):  
    self.log = {}  
  def func1(self):  
    print 'func1()'  
  def sayHello(self):  
    print 'sayHello'  
  def getData(self, input):  
      return input+' from server 1024';  
  
  
if __name__ == '__main__':
    try:
        port = 9090
        handler = HelloServiceHandler()  
        processor = HelloService.Processor(handler)  
        transport = TSocket.TServerSocket(host="127.0.0.1", port=port)  
        tfactory = TTransport.TBufferedTransportFactory()  
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()  
          
        server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)  

      
        print 'Starting the server on %s ...' % str(port)  
        server.serve()  
        print 'done.'  
    except Exception as e:
        print traceback.format_exc()
    
    