import React, { Suspense, lazy } from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from 'react-query'
import { useService } from '@xstate/react'
import ViewAuth from 'views/Auth'
import { authMachineService, STATES as AUTH_STATES } from 'states/auth'

const ViewHome = lazy(() => import(/* webpackChunkName: "authenticated" */ 'views/Home'))

const queryClient = new QueryClient()

function App() {
    const [authState] = useService(authMachineService)

    if (authState.matches(AUTH_STATES.UNAUTHENTICATED)) {
        return (
            <QueryClientProvider client={queryClient}>
                <ViewAuth />
            </QueryClientProvider>
        )
    }

    return (
        <QueryClientProvider client={queryClient}>
            <Router>
                <Suspense fallback={<></>}>
                    <Switch>
                        <Route path="/" component={ViewHome} />
                    </Switch>
                </Suspense>
            </Router>
        </QueryClientProvider>
    )
}

export default App
