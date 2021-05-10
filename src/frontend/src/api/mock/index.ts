import { createServer, Model } from 'miragejs'
import { routes } from 'api/mock/routes'
import { seeds } from 'api/mock/seeds'

/**
 * Create a MirageJS mocking server.
 *
 * Once enabled, it will pick up on
 * connections the application makes,
 * allowing the user to navigate a
 * working application, based on
 * previously prepared mock data.
 */
export function enableMockAPI() {
    createServer({
        routes,
        seeds,

        models: {
            user: Model,
        },
    })
}
