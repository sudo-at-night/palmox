import { Server, Response } from 'miragejs'
import { apiURL } from 'api/client'
import * as ENDPOINTS from 'api/enpoints'

export function routes(this: Server) {
    this.urlPrefix = apiURL || ''

    this.post(
        ENDPOINTS.USER_LOG_IN,
        (schema: any, request) => {
            const body = JSON.parse(request.requestBody)
            const user = schema.users.findBy({ email: body.email })

            if (!user || user.password !== body.password) {
                return new Response(403)
            }

            // Create a new mock session ID, user logged-in
            const newToken = `test-token-${body.email}`
            user.update({ sessionId: newToken })

            // Mock session ID cookie
            document.cookie = `FSESSIONID=${newToken}`

            return new Response(204, {}, {})
        },
        { timing: 1000 }
    )
}
