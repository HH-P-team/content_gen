import "./login.css";

import Input from "../input/input.jsx";
import Button from "../button/button.jsx";
import MenuLink from "../menu/menu-link.jsx";

export default function LoginForm({
  auth,
  error,
  username,
  password,
  confirmPassword,
  onUsername,
  onPassword,
  onConfirmPassword,
  onSubmit,
  isDisabled,
}) {
  return (
    <>
      {!auth && (
        <nav className="sidebar-links">
          <MenuLink path={"/auth"} content={"Зарегистрироваться"} />
        </nav>
      )}

      <form className="login-form" active="#" onSubmit={onSubmit}>
        <div className="login-form__field">
          <Input
            isRequired
            placeholder="Логин"
            value={username}
            onChange={(e) => onUsername(e.target.value)}
          />
        </div>
        <div className="login-form__field">
          <Input
            isRequired
            placeholder="Пароль"
            type="password"
            value={password}
            onChange={(e) => onPassword(e.target.value)}
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
                onChange={(e) => onConfirmPassword(e.target.value)}
              />
            </div>
            <div className="login-form__send">
              <Button
                type="submit"
                text="Зарегистрироваться"
                isDisabled={isDisabled}
              />
            </div>
          </>
        ) : (
          <div className="login-form__send">
            <Button type="submit" text="Войти" isDisabled={isDisabled} />
          </div>
        )}

        {error && <p className="login-form__error">{error}</p>}
      </form>
    </>
  );
}
