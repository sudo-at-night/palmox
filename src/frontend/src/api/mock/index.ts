import { createServer, Model } from 'miragejs'
import { routes } from './routes'
import { seeds } from './seeds'

/**
 * Create a MirageJS mocking server.
 *
 * Once triggered, it will pick up on
 * connections the application makes,
 * allowing the user to navigate a
 * working application, based on
 * previously prepared mock data.
 */
export function triggerMock() {
    createServer({
        routes,
        seeds,

        models: {
            user: Model,
        },
    })
}
