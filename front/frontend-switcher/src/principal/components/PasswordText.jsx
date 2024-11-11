import React, {useState} from "react";
import {
  IconButton,
  InputAdornment,
  FormControl,
  InputLabel,
  OutlinedInput,
  FormHelperText,
} from "@mui/material";
import VisibilityIcon from "@mui/icons-material/Visibility";
import VisibilityOffIcon from "@mui/icons-material/VisibilityOff";

const PasswordText = ({password, setPassword, error}) => {
  const [showPassword, setShowPassword] = useState(true);

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  const handlePasswordChange = (e) => {
    const newValue = e.target.value;
    const regex = /^[0-9]{0,4}$/; // Solo permite hasta 4 dígitos numéricos

    if (regex.test(newValue)) {
      setPassword(newValue);
    }
  };

  return (
    <FormControl color="secondary" variant="outlined" error={error}>
      <InputLabel color="secondary" htmlFor="password">
        PIN
      </InputLabel>
      <OutlinedInput
        id="password"
        type={showPassword ? "password" : "text"}
        value={password}
        onChange={handlePasswordChange}
        inputProps={{maxLength: 4, 'data-testid': 'input-pass'}}
        endAdornment={
          <InputAdornment position="end">
            <IconButton onClick={togglePasswordVisibility} edge="end">
              {showPassword ? <VisibilityOffIcon/> : <VisibilityIcon/>}
            </IconButton>
          </InputAdornment>
        }
        label="PIN"
      />
    </FormControl>
  );
};

export default PasswordText;
