import React, { useEffect, useMemo, useState } from "react";
import Cookies from "js-cookie";

import { UserContext } from "./context.jsx";
import usePrevious from "../hooks/use-previous.jsx";

export default function AuthProvider({ children }) {
  const [isAuthenticated, setAuthenticate] = useState(false);
  const [userData, setUserData] = useState(null);

  const isAuthenticatedPrev = usePrevious(isAuthenticated);

  const setUser = useMemo(
    () => (userData) => {
      setUserData(userData);
      setAuthenticate(true);
    },
    [setAuthenticate]
  );

  const deAuthUser = useMemo(
    () => () => {
      setUserData(null);
      setAuthenticate(false);
    },
    [setAuthenticate]
  );

  useEffect(() => {
    if (isAuthenticatedPrev && !isAuthenticated) {
      setUserData(null);
    }
  }, [isAuthenticated, isAuthenticatedPrev]);

  const value = useMemo(
    () => ({
      userData,
      setUser,
      deAuthUser,
    }),
    [deAuthUser, setUser, userData]
  );

  return <UserContext.Provider value={value}>{children}</UserContext.Provider>;
}
