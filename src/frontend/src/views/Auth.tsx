import React from 'react'
import { Input } from 'components/atoms/Input'
import { Button } from 'components/atoms/Button'
import { ReactComponent as Logo } from 'assets/svg/logo.svg'
import styles from './Auth.module.scss'

export default function ViewAuth() {
    return (
        <>
            <div className={styles.hero}>
                <Logo className={styles.logo} title="Logo" role="image" />
                <p className={styles['logo-text']}>PALMOX</p>
            </div>
            <div className={styles.container}>
                <Input className={styles.input} label="E-Mail" />
                <Input
                    className={styles.input}
                    label="Password"
                    type="password"
                />
                <Button
                    className={`${styles.button} ${styles['button-first']}`}
                >
                    Log In
                </Button>
                <Button className={styles.button} theme="secondary">
                    Register
                </Button>
            </div>
        </>
    )
}
