import React, { FunctionComponent } from 'react'
import styles from './Button.module.scss'

type TButtonProps = {
    className?: string
    onClick?: () => void
    theme?: 'primary' | 'secondary'
}

export const Button: FunctionComponent<TButtonProps> = (props) => {
    const buttonClass = styles[`button-${props.theme}`]

    return (
        <button className={`${buttonClass} ${props.className}`} onClick={props.onClick} type="button">
            {props.children}
        </button>
    )
}

Button.defaultProps = {
    className: '',
    theme: 'primary',
}
