import React from "react";
import SentimentVeryDissatisfiedIcon from "@mui/icons-material/SentimentVeryDissatisfied";
import { Card, CardContent, Box, Typography } from "@mui/material";

const NotAvailableGames = () => {
  return (
    <Card
      variant="outlined"
      sx={{
        marginBottom: 0,
        backgroundColor: "error.light",
        height: {xs: "30px", sm: "40px", md: "44px"},
        width: "100%",
        transition: "transform 0.3s, box-shadow 0.3s",
        boxShadow: 1,
        "&:hover": {
          transform: "translateY(-5px)",
          boxShadow: 2,
        },
      }}
    >
      <CardContent sx={{ padding: 0 }}>
        <Box display="flex" justifyContent="space-between" alignItems="center">
          <Typography variant="h3" component="div" color="white">
            No hay Partidas.
          </Typography>
          <SentimentVeryDissatisfiedIcon
            fontSize="large"
            sx={{ 
              color: "white",
              fontSize: { xs: 30, sm: 36, md: 40 } 
            }}
          />
        </Box>
      </CardContent>
    </Card>
  );
};

export default NotAvailableGames;
