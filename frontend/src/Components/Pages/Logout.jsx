import { useContext, useEffect } from "react";

import { UserContext } from "../../context/context";

import { postLogout}  from "../../api/auth/auth.api";

export default function Logout() {
  const { deAuthUser } = useContext(UserContext);

  const logoutHandler = async () => {
    try {
      await postLogout();

      deAuthUser();
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    logoutHandler();
  }, []);

  return <></>;
}
