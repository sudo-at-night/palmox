import { Server } from 'miragejs'

export function seeds(server: Server) {
    server.create('user', { email: 'test@mail.com', password: 'testme', sessionId: '' } as any)
}
