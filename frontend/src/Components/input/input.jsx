
import React, { useState } from "react";

import './input.css'

export default function Input({
  value,
  placeholder = "",
  autoComplete = "off",
  type = undefined,
  validateText = undefined,
  isValid = true,
  isDisabled = false,
  isRequired = false,
  isActive = false,
  renderIcon = undefined,
  onChange = () => {},
  onFocus = () => {},
  onBlur = () => {},
  readOnly = false,
}) {
  const [isFocus, setFocusStatus] = useState(false);

  function focusHandler() {
    setFocusStatus(true);
    onFocus();
  }

  function blurHandler() {
    setFocusStatus(false);
    onBlur();
  }

  const isFocused = isActive || isFocus;
  const hasPlaceholder = Boolean(value);

  return (
    <div className="input-component-container">
      {(isFocused || hasPlaceholder) && (
        <span
          className={`input-component-container__header${
            isValid ? "" : " not-valid"
          }`}
        >
          {placeholder}
        </span>
      )}
      <input
        className={`input-component${
          renderIcon ? " input-component_icon" : ""
        }${isFocused ? " focus" : ""}${hasPlaceholder ? " placeholder" : ""}`}
        placeholder={isFocused ? "" : placeholder}
        type={type}
        value={value}
        disabled={isDisabled}
        required={isRequired}
        autoComplete={autoComplete}
        onChange={onChange}
        onFocus={focusHandler}
        onBlur={blurHandler}
        readOnly={readOnly}
      />
      {renderIcon && renderIcon()}
      {!isValid && validateText && (
        <span className="input-component__validate">{validateText}</span>
      )}
    </div>
  );
}
