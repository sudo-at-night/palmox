import React, { FunctionComponent } from 'react'
import styles from './Button.module.scss'

type TButtonProps = {
    className?: string
    onClick?: () => void
    theme?: 'primary' | 'secondary'
    type?: 'button' | 'submit'
}

export const Button: FunctionComponent<TButtonProps> = (props) => {
    const buttonClass = styles[`button_${props.theme}`]

    return (
        <button className={`${buttonClass} ${props.className}`} onClick={props.onClick} type={props.type}>
            {props.children}
        </button>
    )
}

Button.defaultProps = {
    className: '',
    theme: 'primary',
    type: 'button',
}
