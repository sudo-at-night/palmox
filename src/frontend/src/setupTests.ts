// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom'

// Global functions we want to mock
window.fetch = jest.fn()

// ENV variables we want to mock
process.env.REACT_APP_API_URL = 'https://test.com'
