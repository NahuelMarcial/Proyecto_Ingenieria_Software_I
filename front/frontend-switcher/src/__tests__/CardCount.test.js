import React from "react";
import CardsCount from "../game/components/CardsCount";
import getCardsCount from "../game/services/GetCardsCount";
import {render, waitFor, screen} from "@testing-library/react";

jest.mock("../game/services/GetCardsCount", () => jest.fn());

const mocksocket = {
	on: jest.fn(),
	off: jest.fn()
};

describe('', () => {
	beforeEach(() => {

	})
	afterEach(() => {
		jest.clearAllMocks();
	})

	it('should render icon', async () => {
		getCardsCount.mockResolvedValueOnce({cantidad: 5});
		render(<CardsCount socket={mocksocket}/>);
		await waitFor(() => {
			expect(screen.getByTestId("deckicon")).toBeInTheDocument();
			expect(screen.getByText("5")).toBeInTheDocument();
		})
	});

	it('should not render icon', async () => {
		getCardsCount.mockResolvedValueOnce({cantidad: 0});
		render(<CardsCount socket={mocksocket}/>);
		await waitFor(() => {
			expect(screen.queryByTestId("deckicon")).not.toBeInTheDocument();
		})
	});

});