import React from "react";
import { createSvgIcon } from "@mui/material/utils";

const AngryFace = createSvgIcon(
  <svg
    width="100"
    height="100"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <circle
      cx="12"
      cy="12"
      r="10"
      fill="#EC1C24"
      stroke="#000"
      strokeWidth="2"
    />
    <ellipse cx="8" cy="11" rx="1.5" ry="2.5" fill="#000" />
    <ellipse cx="16" cy="11" rx="1.5" ry="2.5" fill="#000" />
    <line x1="6.5" y1="6" x2="10.5" y2="8" stroke="#000" strokeWidth="1.5" />
    <line x1="13.5" y1="8" x2="17.5" y2="6" stroke="#000" strokeWidth="1.5" />
    <path d="M8 17 Q12 14, 16 17" stroke="#000" strokeWidth="1.5" fill="none" />
  </svg>,
  "AngryFace"
);

export default AngryFace;
