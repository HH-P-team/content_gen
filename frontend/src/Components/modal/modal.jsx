import { useContext } from "react";

import "./modal.css";

import { AppContext } from "../../context/context.jsx";

export default function Modal({ title, content, contentObject }) {
  const { isModalOpen } = useContext(AppContext);

  const LoginFrom = contentObject.loginForm;
  const auth = contentObject.auth;

  return (
    <div
      className={`${
        isModalOpen ? "modal-overlay show-modal" : "modal-overlay"
      }`}
    >
      <div className="modal-container">
        <p>{title}</p>
        {content && <p>{content}</p>}
        <LoginFrom auth={auth} />
      </div>
    </div>
  );
}
