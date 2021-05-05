import { Machine, interpret } from 'xstate'

export enum STATES {
    AUTHENTICATED = 'authenticated',
    UNAUTHENTICATED = 'unauthenticated',
}

export enum TRANSITIONS {
    TOGGLE,
}

const authMachine = Machine({
    id: 'auth',
    initial: STATES.UNAUTHENTICATED,
    states: {
        [STATES.UNAUTHENTICATED]: {
            on: { [TRANSITIONS.TOGGLE]: STATES.AUTHENTICATED },
        },
        [STATES.AUTHENTICATED]: {
            on: { [TRANSITIONS.TOGGLE]: STATES.UNAUTHENTICATED },
        },
    },
})

/**
 * Auth machine is responsible for managing user's
 * authentication state across all views.
 */
export const authMachineService = interpret(authMachine)
authMachineService.start()
