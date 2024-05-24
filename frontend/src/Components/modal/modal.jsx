import "./modal.css";
import { useContext, useEffect } from "react";
import { Navigate, Outlet } from "react-router-dom";
import { AppContext } from "../../context/context.jsx";

export default function Modal({ title, content, contentObject }) {
  const { isModalOpen, closeModal } = useContext(AppContext);

  // const LoginFrom = contentObject.loginForm;
  // const auth = contentObject.auth;

  return (
    <>
      {isModalOpen ? (
        <div
          className={`${false ? "modal-overlay show-modal" : "modal-overlay"}`}
        >
          <div className="modal-container">
            <p>{title}</p>
            {contentObject}
            {/* <Outlet /> */}
            {/* {{ contentObject }} */}
            {/* {content && <p>{content}</p>} */}
            {/* <LoginFrom auth={auth} /> */}
          </div>
        </div>
      ) : (
        <Navigate to="/" replace />
      )}
    </>
  );
}
