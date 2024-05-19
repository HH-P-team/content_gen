import Modal from "../modal/modal";
import LoginForm from "../auth/login";

export default function Login({ auth }) {
  const contentObject = {
    loginForm: LoginForm,
    auth: auth,
  };

  return (
    <Modal title={"test"} content={"test"} contentObject={contentObject} />
  );
}
