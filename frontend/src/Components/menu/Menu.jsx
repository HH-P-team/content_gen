import { useContext } from "react";
import "./Menu.css";
import MenuButton from "./MenuButton";

import { UserContext } from "../../context/context.jsx";

export default function Menu(props) {
  const { userData } = useContext(UserContext);

  return (
    <div className="Menu">
      <MenuButton path={"/subjects"} name="Категории" />
      <MenuButton path={"/products"} name="Продукты" />
      <MenuButton path={"/posts"} name="Рекламные посты" />
      <MenuButton path={"/profile"} name="Профиль" />
      <MenuButton path={"/about"} name="О проекте" />
      <MenuButton path={"/help"} name="Помощь" />
      {userData && <MenuButton path={"/logout"} name="Выйти" />}
    </div>
  );
}
