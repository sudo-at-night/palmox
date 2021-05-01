import { Machine, interpret } from 'xstate'

export enum STATES {
    AUTHORIZED = 'authorized',
    UNAUTHORIZED = 'unauthorized',
}

const authMachine = Machine({
    id: 'auth',
    initial: STATES.UNAUTHORIZED,
    states: {
        [STATES.UNAUTHORIZED]: {
            on: { TOGGLE: STATES.AUTHORIZED },
        },
        [STATES.AUTHORIZED]: {
            on: { TOGGLE: STATES.UNAUTHORIZED },
        },
    },
})

/**
 * Auth machine is responsible for managing user's
 * authentication state across all views.
 */
export const authMachineService = interpret(authMachine)
authMachineService.start()