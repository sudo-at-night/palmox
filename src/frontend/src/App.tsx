import React, { Suspense, lazy } from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import { useService } from '@xstate/react'
import ViewAuth from 'views/Auth'
import { authMachineService, STATES as AUTH_STATES } from 'states/auth'

const ViewHome = lazy(
    () => import(/* webpackChunkName: "authorized" */ 'views/Home')
)

function App() {
    const [authState] = useService(authMachineService)

    if (authState.matches(AUTH_STATES.UNAUTHENTICATED)) {
        return <ViewAuth />
    }

    return (
        <Router>
            <Suspense fallback={<></>}>
                <Switch>
                    <Route path="/" component={ViewHome} />
                </Switch>
            </Suspense>
        </Router>
    )
}

export default App
