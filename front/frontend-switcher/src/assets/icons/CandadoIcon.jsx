import { createSvgIcon } from "@mui/material/utils";
import "./CandadoIcon.css";

const CandadoIcon = createSvgIcon(
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 27"
    width="30"
    height="35"
    fill="none"
    stroke="black"
    strokeWidth="2"
  >
    <g>
      <rect
        x="6"
        y="12"
        width="12"
        height="10"
        rx="2"
        ry="2"
        stroke="black"
        fill="none"
      />
      <path
        className="lock-top"
        d="M8 12V8a4 4 0 0 1 8 0v4"
        stroke="black"
        fill="none"
      />
      <line
        x1="12"
        y1="15"
        x2="12"
        y2="19"
        stroke="black"
        strokeWidth="2"
        strokeLinecap="round"
      />
    </g>
  </svg>,
  "CandadoIcon"
);

export default CandadoIcon;
