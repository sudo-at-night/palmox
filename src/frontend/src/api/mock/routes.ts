import type { Server } from 'miragejs'

import { Response } from 'miragejs'
import { apiURL } from 'api/client'
import * as ENDPOINTS from 'api/endpoints'

export function routes(this: Server) {
    this.urlPrefix = apiURL || ''
    this.timing = 1000

    this.post(ENDPOINTS.USER_LOGIN, (schema: any, request) => {
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

        return new Response(204, {})
    })
}
