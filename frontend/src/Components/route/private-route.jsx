import React, { useContext } from "react";
import { Navigate, Outlet } from "react-router-dom";

import { UserContext } from "../../context/context.jsx";

export default function PrivateRoute({ redirectPath, children }) {
  const { isAuthenticated } = useContext(UserContext);

  return isAuthenticated ? <Outlet /> : <Navigate to={redirectPath} />;
}
