// src/components/getFaceIcon.js
import React from "react";
import FaceIcon from "@mui/icons-material/Face";
import Face4Icon from "@mui/icons-material/Face4";
import Face5Icon from "@mui/icons-material/Face5";
import Face6Icon from "@mui/icons-material/Face6";

const getFaceIcon = (face, isOccupied) => {
  const iconStyles = {
    fontSize: "clamp(2rem, 5vw, 4rem)",
    color: isOccupied ? "white" : "text.secondary",
    mb: 1,
  };

  switch (face) {
    case 1:
      return <Face4Icon sx={iconStyles} />;
    case 2:
      return <Face5Icon sx={iconStyles} />;
    case 3:
      return <Face6Icon sx={iconStyles} />;
    default:
      return <FaceIcon sx={iconStyles} />;
  }
};

export default getFaceIcon;