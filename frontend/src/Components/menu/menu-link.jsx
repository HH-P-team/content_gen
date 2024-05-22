import React from "react";
import { NavLink } from "react-router-dom";

export default function MenuLink({ path, icon, content }) {
  const getStyleForNavLink = ({ isActive }) =>
    isActive
      ? {
          cursor: "default",
          color: "black",
        }
      : {};

  return (
    <NavLink to={path} style={getStyleForNavLink}>
      {icon} {content}
    </NavLink>
  );
}
