import React from "react"
import {createSvgIcon} from "@mui/material/utils";

const CrownIcon = createSvgIcon(
  <svg
    width="100"
    height="100"
    viewBox="0 0 500 500"
    xmlns="http://www.w3.org/2000/svg"
  >
    <polygon points="100,250 100,400 250,400" fill="#fff"/>
    <polygon points="250,200 160,400 340,400" fill="#fff"/>
    <polygon points="400,250 240,400 400,400" fill="#fff"/>
    <rect x="100" y="400" width="300" height="30" fill="#fff"/>
  </svg>,
  "Crown"
);

export default CrownIcon;
