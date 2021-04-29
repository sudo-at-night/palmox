import React, { FunctionComponent } from 'react'
import styles from './Button.module.scss'

type TButtonProps = {
    onClick?: () => void
}

export const Button: FunctionComponent<TButtonProps> = (props) => {
    return (
        <button className={styles.button} {...props}>
            {props.children}
        </button>
    )
}
