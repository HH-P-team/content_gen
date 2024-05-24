import Modal from "../modal/modal";
import LoginForm from "../auth/login";
import { useState, useContext } from "react";
import { Navigate } from "react-router-dom";
import { postRegistration, postAuthenticate } from "../../api/auth/auth.api.js";
import { UserContext } from "../../context/context.jsx";
import { AppContext } from "../../context/context.jsx";
import { Navigate } from "react-router-dom";

export default function Login({ auth }) {
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
    setError("");
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
            if (data.login) {
              setUser(data);
              console.log("Authent");
              closeModal();
            }
            console.log(data);
          })
          .catch((err) => setError(err.response.data.detail));
      } else {
        postAuthenticate(username, password)
          .then((data) => {
            if (data.login) {
              setUser(data);
              console.log("Authent");
              closeModal();
            }
            console.log(data);
          })
          .catch((err) => setError(err.response.data.detail));
      }
    } catch (error) {
      console.error(error);
      setError(error.message);
    }
    disable(false);
  };

  const submitHandler = (e) => {
    e.preventDefault();
    onSubmit();
  };

  if (isAuthenticated) {
    return <Navigate to=".." replace />;
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
