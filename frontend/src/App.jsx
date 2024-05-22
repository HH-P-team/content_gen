import "./App.css";
import { useState, useEffect, useMemo, useContext } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./Components/App/Header/Header";
import Footer from "./Components/App/Footer/Footer";
import Sidebar from "./Components/App/Sidebar/Sidebar";
import Subjects from "./Components/Pages/Subjects";
import Products from "./Components/Pages/Products";
import Posts from "./Components/Pages/Posts";
import Profile from "./Components/Pages/Profile";
import About from "./Components/Pages/About";
import Help from "./Components/Pages/Help";
import Login from "./Components/Pages/Login";
import Logout from "./Components/Pages/Logout";
import NotFound from "./Components/Pages/NotFound";
import PrivateRoute from "./Components/route/private-route";
import { postCheck } from "./api/auth/auth.api";
import Cookies from "js-cookie";

import { UserContext } from "./context/context";

export default function App() {
  const [data, setData] = useState([]);
  const { setUser } = useContext(UserContext);

  const fetch = useMemo(
    () => async () => {
      data = await postCheck(Cookies.get("access_token"));
      if (data.login) {
        setUser(data);
      }
    },
    [setUser]
  );

  useEffect(() => {
    fetch();
  }, []);

  return (
    <div className="App">
      <BrowserRouter>
        <Sidebar />
        <div className="Wrapper">
          <Header />
          <Routes>
            <Route path="/">
              <Route path="subjects" element={<Subjects data={data} />} />
              <Route path="products" element={<Products data={data} />} />
              <Route path="posts" element={<Posts />} />
              <Route path="about" element={<About />} />
              <Route path="help" element={<Help />} />
              <Route element={<PrivateRoute redirectPath={"login"} />}>
                <Route path="profile" element={<Profile />} />
                <Route path="logout" element={<Logout />} />
              </Route>
              <Route path="login" element={<Login auth={false} />} />
              <Route path="auth" element={<Login auth={true} />} />
              <Route path="*" element={<NotFound />} />
            </Route>
          </Routes>
          <Footer />
        </div>
      </BrowserRouter>
    </div>
  );
}
