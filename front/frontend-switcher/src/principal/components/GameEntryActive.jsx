import React, {useEffect} from "react"
import {Box, Card, CardContent, Typography} from "@mui/material"

const GameEntryActive = ({gameName, gameState, isMyTurn}) => {
	return (
		<Card variant="outlined"
			  sx={{
				  position: "relative",
				  marginBottom: 0, // Ajuste de espaciado según el theme
				  backgroundColor: "primary.main", // Usar color primario desde el tema
				  height: "44px",
				  transition: "transform 0.3s, box-shadow 0.3s",
				  boxShadow: 1, // Usar el primer nivel de sombras del tema
				  "&:hover": {
					  transform: "translateY(-5px)",
					  boxShadow: 2, // Usar el segundo nivel de sombras del tema
				  },
			  }}>
			<CardContent sx={{padding: 0}}>
				<Box display="flex" justifyContent="space-between" alignItems="center">
					<Typography variant="h3" component="div">
						{gameName}
					</Typography>
					<Typography variant="h3" component="div">
						{gameState}
					</Typography>
					<Typography variant="h3" component="div">
						{isMyTurn}
					</Typography>
				</Box>
			</CardContent>
		</Card>
	);
};

export default GameEntryActive;