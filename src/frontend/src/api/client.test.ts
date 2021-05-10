import { client } from './client'

describe('API Client', () => {
    test('call() -> prepends REACT_APP_API_URL to each request', () => {
        client.call('/endpoint', {})

        expect(fetch).toHaveBeenCalledWith('https://test.com/endpoint', {})
    })

    test.each`
        scheme
        ${'http://'}
        ${'https://'}
        ${'HTTP://'}
        ${'HTTPS://'}
        ${'www.'}
        ${'WWW.'}
    `(
        'call() -> does not prepend REACT_APP_API_URL if a full URL is passed, scheme: $scheme',
        ({ scheme }) => {
            const urlToCall = `${scheme}test2.com/endpoint`

            client.call(urlToCall, {})

            expect(fetch).toHaveBeenCalledWith(urlToCall, {})
        }
    )
})
