import React from 'react';
import {render, screen, fireEvent} from '@testing-library/react';
import BotonAbandonarPartida from "../lobby/components/BotonAbandonarPartida";

describe("Disconect test", () => {
	test("show button", () => {
		const fun = jest.fn();
		render(<BotonAbandonarPartida onClick={fun}/>);
		const buttontext = screen.getByText("Abandonar Partida");
		expect(buttontext).toBeInTheDocument();
	});
	test("Press Button", () => {
		const fun = jest.fn();
		render(<BotonAbandonarPartida onClick={fun}/>);
		const buttontext = screen.getByText("Abandonar Partida");
		expect(buttontext).toBeInTheDocument();
		fireEvent.click(buttontext);
		expect(fun).toHaveBeenCalled();
	})
})