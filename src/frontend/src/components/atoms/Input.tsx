import type { FunctionComponent } from 'react'
import type { FieldProps } from 'formik'

import React from 'react'
import styles from './Input.module.scss'

type TInputProps = FieldProps & {
    className?: string
    type?: 'text' | 'password'
    disabled?: boolean
    label: string
}

export const Input: FunctionComponent<TInputProps> = (props) => {
    const error = props.form.touched[props.field.name] ? props.form.errors[props.field.name] : null

    let containerClass = props.disabled ? styles.container_disabled : styles.container
    const inputClass = props.field.value ? styles.input_primary : styles.input_empty
    const labelClass = props.field.value ? styles.label_above : styles.label_placeholder

    if (error) {
        containerClass = styles.container_error
    }

    return (
        <div className={`${containerClass} ${props.className}`}>
            <label className={labelClass} htmlFor={props.field.name}>
                {props.label}
            </label>
            <input
                id={props.field.name}
                className={inputClass}
                type={props.type}
                onBlur={props.field.onBlur}
                onChange={props.field.onChange}
                disabled={props.disabled}
                data-testid="input-input"
            >
                {props.children}
            </input>
            {error ? (
                <p className={styles.error} data-testid="input-error">
                    {error}
                </p>
            ) : null}
        </div>
    )
}

Input.defaultProps = {
    className: '',
    type: 'text',
    disabled: false,
}
