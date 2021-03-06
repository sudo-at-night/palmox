import React from 'react'
import { render, screen, fireEvent } from '@testing-library/react'
import { Button } from './Button'

test('Button -> renders without crashing', () => {
    render(<Button>Hello</Button>)
    expect(screen.getByText('Hello')).toBeInTheDocument()
})

test('Button -> onClick is emitted after clicking the button', () => {
    const onClick = jest.fn()

    render(<Button onClick={onClick}>Hello</Button>)

    fireEvent.click(screen.getByText('Hello'))

    expect(onClick).toHaveBeenCalled()
})

test('Button -> onClick is not emitted after clicking the button if button is disabled', () => {
    const onClick = jest.fn()

    render(
        <Button onClick={onClick} disabled>
            Hello
        </Button>
    )

    fireEvent.click(screen.getByText('Hello'))

    expect(onClick).not.toHaveBeenCalled()
})
