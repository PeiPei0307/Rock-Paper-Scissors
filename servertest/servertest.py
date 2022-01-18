import asyncio, zen_utils, time

class ZenServer(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.data = b''
        print('Accepted connection from {}'.format(self.address))

    def data_received(self, data):
        if data == b'|exit|':
            self.transport.write(b'Farewell, client.')
        #print('  Incoming ', len(data), '-octet message:', repr(data))
        if data == b'testdata1':
            self.transport.write(b'Continue.')
        if data == b'testdata2':
            self.transport.write(b'TTTTT Continue.')
        if data == b'testdata3':
            self.transport.write(b'FFFFF Continue.')

    def connection_lost(self, exc):
        if exc:
            print('Client {} error: {}'.format(self.address, exc))
        elif self.data:
            print('Client {} sent {} but then closed'
                  .format(self.address, self.data))
        else:
            print('Client {} closed socket'.format(self.address))

if __name__ == '__main__':
    address = zen_utils.parse_command_line('asyncio server using callbacks')
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ZenServer, *address)
    server = loop.run_until_complete(coro)
    print('Listening at {}'.format(address))
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()
