import type { FieldProps } from 'formik'

import React from 'react'
import { render, screen, fireEvent } from '@testing-library/react'
import { cloneDeep as clone } from 'lodash'
import { Input } from './Input'

/**
 * Mock formik props since Input component
 * is tightly bound to being used as
 * Formik's field component.
 */
const defaultMockFormikProps: any = {
    field: {
        value: '',
        name: 'test-field',
        onBlur: jest.fn(),
        onChange: jest.fn(),
    },
    form: {
        touched: {
            'test-field': false,
        },
        errors: {
            'test-field': '',
        },
    },
}

function setup() {
    return {
        mockFormikProps: clone(defaultMockFormikProps),
    }
}

test('Input -> renders without crashing', () => {
    const { mockFormikProps } = setup()

    render(<Input label="Test Input" {...mockFormikProps} />)

    expect(screen.getByTestId('input-input')).toBeInTheDocument()
})

test('Input -> renders disabled input without crashing', () => {
    const { mockFormikProps } = setup()

    render(<Input label="Test Input" disabled {...mockFormikProps} />)

    expect(screen.getByTestId('input-input')).toBeInTheDocument()
})

test('Input -> renders input with value without crashing', () => {
    const { mockFormikProps } = setup()
    mockFormikProps.field.value = 'changed value'

    render(<Input label="Test Input" {...mockFormikProps} />)

    expect(screen.getByTestId('input-input')).toBeInTheDocument()
})

test('Input -> onBlur is emitted via Formik props on blur', () => {
    const { mockFormikProps } = setup()

    render(<Input label="Test Input" {...mockFormikProps} />)

    const elUnderTest = screen.getByTestId('input-input')

    fireEvent.focus(elUnderTest)
    fireEvent.blur(elUnderTest)

    expect(mockFormikProps.field.onBlur).toHaveBeenCalled()
})

test('Input -> onChange is emitted via Formik props on value change', () => {
    const { mockFormikProps } = setup()

    render(<Input label="Test Input" {...mockFormikProps} />)

    const elUnderTest = screen.getByTestId('input-input')

    fireEvent.change(elUnderTest, { target: { value: 'changed value' } })

    expect(mockFormikProps.field.onChange).toHaveBeenCalled()
})

test('Input -> error is rendered', () => {
    const { mockFormikProps } = setup()
    mockFormikProps.form.errors['test-field'] = 'Input is incorrect'
    mockFormikProps.form.touched['test-field'] = true

    render(<Input label="Test Input" {...mockFormikProps} />)

    expect(screen.getByTestId('input-error')).toBeInTheDocument()
})
