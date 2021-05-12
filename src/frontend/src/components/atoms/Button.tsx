import React, { FunctionComponent } from 'react'
import styles from './Button.module.scss'

type TButtonProps = {
    onClick?: () => void
    className?: string
    theme?: 'primary' | 'secondary'
    type?: 'button' | 'submit'
    disabled?: boolean
}

export const Button: FunctionComponent<TButtonProps> = (props) => {
    const buttonClass = props.disabled
        ? styles[`button_${props.theme}_disabled`]
        : styles[`button_${props.theme}`]

    return (
        <button
            className={`${buttonClass} ${props.className}`}
            onClick={props.onClick}
            type={props.type}
            disabled={props.disabled}
        >
            {props.children}
        </button>
    )
}

Button.defaultProps = {
    className: '',
    theme: 'primary',
    type: 'button',
}
