import React from 'react'
import { useService } from '@xstate/react'
import { authMachineService } from 'states/auth'
import { Button } from 'components/atoms/Button'

export default function ViewAuth() {
    const [, authSend] = useService(authMachineService)

    return (
        <>
            <Button onClick={() => authSend('TOGGLE')}>Authorize</Button>
        </>
    )
}
