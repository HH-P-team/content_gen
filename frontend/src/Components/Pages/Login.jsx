import Modal from "../modal/modal";
import LoginForm from "../auth/login";

import { useState, useContext } from "react";
import Cookies from "js-cookie";
import { Navigate } from "react-router-dom";

// import "./login.css";

import Input from "../input/input.jsx";
import Button from "../button/button.jsx";
import MenuLink from "../menu/menu-link.jsx";
import { postRegistration, postAuthenticate } from "../../api/auth/auth.api.js";
// import checkUser from "../../hooks/check-user.jsx";
import { UserContext } from "../../context/context.jsx";
import { AppContext } from "../../context/context.jsx";

export default function Login({ auth }) {
  // const contentObject = {
  //   loginForm: LoginForm,
  //   auth: auth,
  // };

  const [error, setError] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [isDisabled, disable] = useState(false);

  const { setUser, isAuthenticated } = useContext(UserContext);
  const { closeModal } = useContext(AppContext);

  const usernameHandler = (username) => {
    setError("");
    setUsername(username);
  };

  const passwordHandler = (password) => {
    setError("");
    setPassword(password);
  };

  const confirmPasswordHandler = (confirmPassword) => {
    setError("");
    setConfirmPassword(confirmPassword);
  };

  const onSubmit = async () => {
    disable(true);

    if (auth && password !== confirmPassword) {
      setError("Пароли не совпадают");
      disable(false);
      return;
    }

    try {
      if (auth) {
        postRegistration(username, password)
          .then((data) => {
            // setUser(data);

            if (
              //   Cookies.get("access_token") &&
              //   Cookies.get("refresh_token") &&
              data.login
            ) {
              setUser(data);
              //   closeSidebar();
            }
            // checkUser(data);
            console.log(data);
          })
          .catch((err) => setError(err.message));
      } else {
        postAuthenticate(username, password)
          .then((data) => {
            if (
              //   Cookies.get("access_token") &&
              //   Cookies.get("refresh_token") &&
              data.login
            ) {
              setUser(data);
              //   closeSidebar();
            }
            // checkUser(data);
            console.log(data);
          })
          .catch((err) => setError(err.message));
        // return <Navigate to="/" replace />;
      }

      // data = await postLogin();
      // console.log(data);
      // setTimeout(1);
      // const response = await axios({
      //   method: "POST",
      //   url: "/auth/login",
      //   data: {
      //     username,
      //     password,
      //   },
      // });
      // if (cookie.get(CSRF_TOKEN_COOKIE_KEY) && response.data.username) {
      //   setUser(response.data);
      // }
    } catch (error) {
      console.error(error);
      setError(error);
    }
    disable(false);
    // return <Navigate to="/" replace />;
    closeModal();
  };

  const submitHandler = (e) => {
    e.preventDefault();
    onSubmit();
    // return <Navigate to="/" replace />;
  };

  if (isAuthenticated) {
    return <Navigate to="/" replace />;
  }

  return (
    <Modal
      title={"Авторизация"}
      contentObject={
        <LoginForm
          auth={auth}
          error={error}
          username={username}
          password={password}
          confirmPassword={confirmPassword}
          onUsername={usernameHandler}
          onPassword={passwordHandler}
          onConfirmPassword={confirmPasswordHandler}
          onSubmit={submitHandler}
          isDisabled={isDisabled}
        />
      }
    />
  );
}
