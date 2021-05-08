export const apiURL = process.env.REACT_APP_API_URL

/**
 * API client for the application.
 */
export const client = {
    /**
     * Simple wrapper around native "fetch" to allow
     * config to contain global API configuration options.
     */
    call(url: string, config: any) {
        const urlToCall = `${apiURL}${url}`
        return fetch(urlToCall, config)
    },
}
