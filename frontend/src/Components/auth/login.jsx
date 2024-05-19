import { useState } from "react";

import "./login.css";

import Input from "../input/input.jsx";
import Button from "../button/button.jsx";
import MenuLink from "../menu/menu-link.jsx";

export default function LoginForm({ auth }) {
  const [error, setError] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [isDisabled, disable] = useState(false);

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
      setTimeout(1);
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
  };

  const submitHandler = (e) => {
    e.preventDefault();
    onSubmit();
  };

  return (
    <>
      {!auth && (
        <nav className="sidebar-links">
          <MenuLink path={"/auth"} content={"Зарегистрироваться"} />
        </nav>
      )}

      <form className="login-form" active="#" onSubmit={submitHandler}>
        <div className="login-form__field">
          <Input
            isRequired
            placeholder="Логин"
            value={username}
            onChange={(e) => usernameHandler(e.target.value)}
          />
        </div>
        <div className="login-form__field">
          <Input
            isRequired
            placeholder="Пароль"
            type="password"
            value={password}
            onChange={(e) => passwordHandler(e.target.value)}
          />
        </div>
        {auth ? (
          <>
            <div className="login-form__field">
              <Input
                isRequired
                placeholder="Подтверждения пароля"
                type="password"
                value={confirmPassword}
                onChange={(e) => confirmPasswordHandler(e.target.value)}
              />
            </div>
            <div className="login-form__send">
              <Button
                type="submit"
                text="Зарегистрироваться"
                style="primary"
                isDisabled={isDisabled}
              />
            </div>
          </>
        ) : (
          <div className="login-form__send">
            <Button
              type="submit"
              text="Войти"
              style="primary"
              isDisabled={isDisabled}
            />
          </div>
        )}

        {error && <p className="login-form__error">{error}</p>}
      </form>
    </>
  );
}
