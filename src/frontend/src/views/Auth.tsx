import React from 'react'
import { useService } from '@xstate/react'
import { authMachineService } from 'states/auth'

export default function ViewAuth() {
    const [, authSend] = useService(authMachineService)

    return (
        <>
            <button onClick={() => authSend('TOGGLE')}>Authorize</button>
        </>
    )
}
