import React from 'react';
import {render, screen, fireEvent, queryByRole} from '@testing-library/react';
import Setnickname from '../principal/components/createUserName';

describe('CreateUserName Component', () => {
	test('should render input field', () => {
		render(<Setnickname/>);
		const inputElement = screen.getByText("Ingrese su nombre de jugador");
		expect(inputElement).toBeInTheDocument();
	});

	test('should update input value on change', () => {
		render(<Setnickname/>);
		const inputElement = screen.getByLabelText("nickname");
		fireEvent.change(inputElement, {target: {value: 'newUser'}});
		expect(inputElement.value).toBe('newUser');
	});

	test('should trigger submit function on button click', () => {
		const handleSubmit = jest.fn();
		render(<Setnickname/>);
		const inputElement = screen.getByLabelText("nickname");
		const buttonElement = screen.getByText("Guardar");
		fireEvent.change(inputElement, {target: {value: 'newUser'}});
		expect(buttonElement).not.toBeDisabled();
		fireEvent.click(buttonElement);
		expect(sessionStorage.getItem("jugador_nombre")).toBe("newUser");
	});
})