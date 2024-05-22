import React from "react";

import './button.css'

export default function Button({
  text,
  type = "button",
  style = "default",
  isActive = false,
  isDisabled = false,
  onClick = () => undefined,
}) {
  return (
    <button
      className={`button button_${style}${isActive ? " active" : ""}`}
      type={type}
      disabled={isDisabled}
      onClick={onClick}
    >
      {isDisabled ? "Submitting..." : text}
    </button>
  );
}
