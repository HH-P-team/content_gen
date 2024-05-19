import { useContext, useEffect } from "react";

// import { UserContext, ApiContext, CookieContext } from "../context/context.jsx";

// import { CSRF_TOKEN_COOKIE_KEY } from "../constants/constants.jsx";

export default function Logout() {
  // const cookie = useContext(CookieContext);
  // const { axios } = useContext(ApiContext);
  // const { deAuthUser } = useContext(UserContext);

  // const logoutHandler = async () => {
  //   try {
  //     await axios({
  //       method: "POST",
  //       url: "/auth/logout",
  //       headers: {
  //         "X-CSRFToken": cookie.get(CSRF_TOKEN_COOKIE_KEY),
  //       },
  //     });

  //     deAuthUser();
  //     cookie.delete(CSRF_TOKEN_COOKIE_KEY);
  //   } catch (error) {
  //     console.error(error);
  //   }
  // };

  // useEffect(() => {
  //   logoutHandler();
  // }, []);

  return null;
}
