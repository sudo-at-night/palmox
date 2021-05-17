jest.mock('api/client', () => ({
    client: {
        call: jest.fn(),
    },
}))

import { client } from 'api/client'
import * as CALLS from './calls'

const call = <jest.MockedFunction<typeof client.call>>client.call

test('Log In -> Uses email and password to call the API with JSON string', () => {
    const credentials = { email: 'username@mail.com', password: 'secret' }

    CALLS.callLogIn(credentials)

    const callArgs = call.mock.calls[0][1]
    const callBody = JSON.parse(callArgs.body)

    expect(callBody).toEqual(credentials)
})

test('Log Out -> Calls the API', () => {
    CALLS.callLogOut()

    expect(call).toHaveBeenCalledWith('/logout', { method: 'GET' })
})

test('Register -> Uses email, password and confirmation of password to call the API with JSON string', () => {
    const credentials = { email: 'username@mail.com', password: 'secret', confirmPassword: 'secret' }

    CALLS.callRegister(credentials)

    const callArgs = call.mock.calls[0][1]
    const callBody = JSON.parse(callArgs.body)

    expect(callBody).toEqual(credentials)
})
