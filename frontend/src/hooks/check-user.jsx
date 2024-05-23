import { useContext } from "react";
import Cookies from "js-cookie";

import { UserContext } from "../context/context.jsx";
import { AppContext } from "../context/context.jsx";

export default function checkUser(data) {
  const { setUser } = useContext(UserContext);
  const { closeSidebar } = useContext(AppContext);

  if (
    Cookies.get("access_token") &&
    Cookies.get("refresh_token") &&
    data.login
  ) {
    setUser(data);
    closeSidebar();
  }
}
