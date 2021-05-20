import { client } from 'api/client'
import * as ENDPOINTS from 'api/endpoints'

export type TCallLogInArgs = {
    email: string
    password: string
}

/**
 * Log the user in
 */
export function callLogIn(args: TCallLogInArgs) {
    const { email, password } = args

    return client.call(ENDPOINTS.USER_LOGIN, {
        method: 'POST',
        body: JSON.stringify({ email, password }),
    })
}

/**
 * Log the user out
 */
export function callLogOut() {
    return client.call(ENDPOINTS.USER_LOGOUT, {
        method: 'GET',
    })
}

export type TCallRegisterArgs = {
    email: string
    password: string
}

/**
 * Register new user
 */
export function callRegister(args: TCallRegisterArgs) {
    const { email, password } = args

    return client.call(ENDPOINTS.USER_REGISTER, {
        method: 'POST',
        body: JSON.stringify({ email, password }),
    })
}
