import { client } from 'api/client'
import * as ENDPOINTS from 'api/enpoints'

export type TCallLogInArgs = {
    email: string
    password: string
}

/**
 * Log the user in
 */
export function callLogIn(args: TCallLogInArgs) {
    const { email, password } = args

    return client.call(ENDPOINTS.USER_LOG_IN, {
        method: 'POST',
        body: JSON.stringify({ email, password }),
    })
}
