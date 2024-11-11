import React, { useEffect, useState } from "react";
import { Box, IconButton, Typography } from "@mui/material";
import LockIcon from "@mui/icons-material/Lock";
import LockOpenIcon from "@mui/icons-material/LockOpen";
import PasswordText from "./PasswordText";

const PasswordInput = ({ setPassword, isPrivate }) => {
  const [localPassword, setLocalPassword] = useState("");
  const [error, setError] = useState(false);

  const handlePasswordChange = (newPassword) => {
    setLocalPassword(newPassword);
    setPassword(newPassword);
  };

  useEffect(() => {
    setError(
      isPrivate && localPassword.length !== 0 && localPassword.length !== 4
    );
  }, [localPassword, isPrivate]);

  return (
    <div>
      <Typography 
        variant="body2" 
        color="text.secondary" 
        sx={{ 
          ml: 1, 
          fontSize: { xs: "0.7rem", sm: "0.9rem",}
        }}
      >
        Contraseña (Opcional)
      </Typography>
      <Box
        padding={1}
        sx={{
          display: "flex",
          alignItems: "center",
        }}
      >
        <Box
          sx={{
            display: "flex",
            alignItems: "center",
            border: "2px solid",
            borderColor: isPrivate ? "primary.main" : "#bbb",
            borderRadius: 1,
          }}
        >
          <IconButton disabled={true}>
            {isPrivate ? (
              <LockIcon 
                fontSize="large" 
                sx={{ 
                  color: "primary.main",
                  fontSize: { xs: "1.7rem", sm: "2.3rem" }, 
                }} 
              />
            ) : (
              <LockOpenIcon 
                fontSize="large" 
                sx={{ 
                  color: "#bbb",
                  fontSize: { xs: "1.7rem", sm: "2.3rem" }, 
                }} 
              />
            )}
          </IconButton>
        </Box>
        <Box sx={{ ml: 2 }}>
          <PasswordText
            password={localPassword}
            setPassword={handlePasswordChange}
            error={error}
          />
        </Box>
      </Box>
    </div>
  );
};

export default PasswordInput;
