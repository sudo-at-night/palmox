import React, { useRef, useState, FunctionComponent } from 'react'
import random from 'randomstring'
import styles from './Input.module.scss'

type TInputProps = {
    className?: string
    type?: 'text' | 'password'
    disabled?: boolean
    label: string
}

export const Input: FunctionComponent<TInputProps> = (props) => {
    const id = useRef(random.generate())
    const [value, setValue] = useState('')
    const inputClass = value ? styles[`input-primary`] : styles['input-empty']
    const containerClass = props.disabled
        ? styles['container-disabled']
        : styles['container']
    const labelClass = value ? styles['label-below'] : styles['label-above']

    return (
        <div className={`${containerClass} ${props.className}`}>
            <label className={labelClass} htmlFor={id.current}>
                {props.label}
            </label>
            <input
                id={id.current}
                className={inputClass}
                type="text"
                onChange={(e) => setValue(e.target.value)}
                disabled={props.disabled}
            >
                {props.children}
            </input>
        </div>
    )
}

Input.defaultProps = {
    className: '',
    type: 'text',
    disabled: false,
}
