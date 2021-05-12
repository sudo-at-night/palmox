import React, { useState } from 'react'
import { Motion, spring } from 'react-motion'
import { useMutation } from 'react-query'
import { Formik, Field, Form } from 'formik'
import * as Yup from 'yup'
import { TCallLogInArgs, callLogIn, TCallRegisterArgs, callRegister } from 'api/calls'
import { springConfig } from 'configs/spring'
import { Input } from 'components/atoms/Input'
import { Button } from 'components/atoms/Button'
import { ReactComponent as Logo } from 'assets/svg/logo.svg'
import styles from './Auth.module.scss'

type TViewMode = 'login' | 'register'

type TFormProps = {
    onSetMode: (newMode: TViewMode) => void
}

export default function ViewAuth() {
    const [mode, setMode] = useState<TViewMode>('login')
    const [inTransition, setInTransition] = useState<boolean>(false)

    const ActiveForm = mode === 'login' ? FormLogin : FormRegister

    function transitionToMode(newMode: TViewMode) {
        setInTransition(true)
        setTimeout(() => {
            setMode(newMode)
            setInTransition(false)
        }, 400)
    }

    const transitions = {
        from: {
            y: inTransition ? 0 : 40,
            opacity: inTransition ? 1 : 0,
        },
        to: {
            y: inTransition ? spring(40, springConfig) : spring(0, springConfig),
            opacity: inTransition ? spring(0, springConfig) : spring(1, springConfig),
        },
    }

    return (
        <>
            <div className={styles.hero}>
                <Logo className={styles.logo} title="Logo" role="image" />
                <p className={styles.logoText}>PALMOX</p>
            </div>
            <div className={styles.container}>
                <Motion defaultStyle={transitions.from} style={transitions.to}>
                    {(interpolation) => (
                        <div
                            style={{
                                opacity: interpolation.opacity,
                                transform: `translateY(${interpolation.y}px)`,
                            }}
                        >
                            <ActiveForm onSetMode={transitionToMode} />
                        </div>
                    )}
                </Motion>
            </div>
        </>
    )
}

function FormLogin(props: TFormProps) {
    const { mutate: logInUser, isLoading } = useMutation((credentials: TCallLogInArgs) =>
        callLogIn(credentials)
    )

    const initialValues = {
        email: '',
        password: '',
    }

    const formValidation = Yup.object().shape({
        email: Yup.string().required('E-Mail is required.').email('Enter a valid E-Mail.'),
        password: Yup.string()
            .required('Password is required.')
            .min(3, 'Password has to have at least 3 characters.'),
    })

    async function onSubmit(values: any) {
        const { email, password } = values

        logInUser({ email, password })
    }

    return (
        <Formik initialValues={initialValues} onSubmit={onSubmit} validationSchema={formValidation}>
            <Form className={styles.inputs}>
                <Field
                    className={styles.input}
                    component={Input}
                    name="email"
                    label="E-Mail"
                    disabled={isLoading}
                />
                <Field
                    className={styles.input}
                    component={Input}
                    name="password"
                    label="Password"
                    type="password"
                    disabled={isLoading}
                />

                <Button
                    className={`${styles.button} ${styles.button_first}`}
                    type="submit"
                    disabled={isLoading}
                >
                    Log In
                </Button>
                <Button
                    className={styles.button}
                    theme="secondary"
                    onClick={() => props.onSetMode('register')}
                    disabled={isLoading}
                >
                    Register
                </Button>
            </Form>
        </Formik>
    )
}

function FormRegister(props: TFormProps) {
    const { mutate: registerUser, isLoading } = useMutation((credentials: TCallRegisterArgs) =>
        callRegister(credentials)
    )

    const initialValues = {
        email: '',
        password: '',
        confirmPassword: '',
    }

    const formValidation = Yup.object().shape({
        email: Yup.string().required('E-Mail is required.').email('Enter a valid E-Mail.'),
        password: Yup.string()
            .required('Password is required.')
            .min(3, 'Password has to have at least 3 characters.')
            .oneOf([Yup.ref('confirmPassword'), null], 'Both passwords must match.'),
        confirmPassword: Yup.string()
            .required('Password is required.')
            .min(3, 'Password has to have at least 3 characters.')
            .oneOf([Yup.ref('password'), null], 'Both passwords must match.'),
    })

    function onSubmit(values: any) {
        const { email, password, confirmPassword } = values

        registerUser({ email, password, confirmPassword })
    }

    return (
        <Formik initialValues={initialValues} onSubmit={onSubmit} validationSchema={formValidation}>
            <Form className={styles.inputs}>
                <Field
                    className={styles.input}
                    component={Input}
                    name="email"
                    label="E-Mail"
                    disabled={isLoading}
                />
                <Field
                    className={styles.input}
                    component={Input}
                    name="password"
                    label="Password"
                    type="password"
                    disabled={isLoading}
                />
                <Field
                    className={styles.input}
                    component={Input}
                    name="confirmPassword"
                    label="Confirm Password"
                    type="password"
                    disabled={isLoading}
                />

                <Button
                    className={`${styles.button} ${styles.button_first}`}
                    type="submit"
                    disabled={isLoading}
                >
                    Register
                </Button>
                <Button
                    className={styles.button}
                    theme="secondary"
                    onClick={() => props.onSetMode('login')}
                    disabled={isLoading}
                >
                    Log In
                </Button>
            </Form>
        </Formik>
    )
}
