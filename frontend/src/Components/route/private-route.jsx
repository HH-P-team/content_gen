import React, { useContext } from "react";
import { Navigate, Outlet } from "react-router-dom";

// import { ApiContext } from "../../context/context.jsx";

export default function PrivateRoute({ redirectPath }) {
  // const { isAuthenticated } = useContext(ApiContext);
  const { isAuthenticated } = true;

  return isAuthenticated ? <Outlet /> : <Navigate to={redirectPath} />;
}
