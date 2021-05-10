jest.mock('api/client', () => ({
    client: {
        call: jest.fn(),
    },
}))

import { client } from 'api/client'
import * as CALLS from './calls'

const call = <jest.Mock>client.call

test('Log In -> Uses email and password to call the API with JSON string', () => {
    const credentials = { email: 'username@mail.com', password: 'secret' }

    CALLS.callLogIn(credentials)

    const callArgs = call.mock.calls[0][1]
    const callBody = JSON.parse(callArgs.body)

    expect(callBody).toEqual(callBody)
})
