import React from "react";
import {createSvgIcon} from "@mui/material/utils";

const DeckIcon = createSvgIcon(
  <svg
    width="100"
    height="100"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <rect
      x="8"
      y="1.5"
      width="13.5"
      height="20"
      rx="2"
      ry="2"
      fill="none"
      stroke="rgba(242,242,242,0.713)"
      strokeWidth="1.5"
    />
    <rect x="6" y="3" width="14" height="20" rx="2" ry="2" fill="#FFFFFF"/>
  </svg>,
  "DeckIcon"
);

export default DeckIcon;
