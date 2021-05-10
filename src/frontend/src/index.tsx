import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'
import reportWebVitals from './reportWebVitals'
import './scss/index.scss'

if (Boolean(process.env.REACT_APP_API_MOCK)) {
    import('api/mock').then((mock) => mock.enableMockAPI())
}

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
)

reportWebVitals(console.log)
