import sys, glob  
sys.path.append("gen-py")
from myThrift import HelloService  
from myThrift.ttypes import *  
  
  
from thrift import Thrift  
from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
import traceback
  

if __name__ == '__main__':
  try:  
    
    # Make socket  
    transport = TSocket.TSocket('localhost', 9090)  
    
    # Buffering is critical. Raw sockets are very slow  
    transport = TTransport.TBufferedTransport(transport)  
    
    # Wrap in a protocol  
    protocol = TBinaryProtocol.TBinaryProtocol(transport)  
    
    # Create a client to use the protocol encoder  
    client = HelloService.Client(protocol)  
    
    # Connect!  
    transport.open()  

    client.sayHello()
    
    print(client.getData("client access"))  
    # Close!  
    transport.close()  
    
  except Thrift.TException, tx:  
    print traceback.format_exc()
    print '%s' % (tx.message)  