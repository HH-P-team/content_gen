import "./App.css";
import { useState, useEffect, useContext } from "react";
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
import getAllSubjects from "./api/subjects/subject.api";
import Cookies from "js-cookie";

import { UserContext } from "./context/context";

export default function App() {
  const [data, setData] = useState([]);

  // const fetch = useMemo(
  //   () => async () => {
  //     try {
  //       const response = await axios.get("/auth/me");
  //       if (cookie.get(CSRF_TOKEN_COOKIE_KEY) && response.data.username) {
  //         setUser(response.data);
  //       }

  //       const translate = await axios.get("/system/front");
  //       if (translate.data) {
  //         setTranslate(translate.data);
  //       }
  //     } catch (error) {
  //       console.error(error);
  //     }

  //     setLoading(false);
  //   },
  //   [axios, cookie, setUser]
  // );

  // useEffect(() => {
  //   fetch();
  // }, []);

  const { setUser } = useContext(UserContext);

  useEffect(() => {
    if (Cookies.get("access_token") && Cookies.get("refresh_token")) {
      setUser();
    }
  }, []);

  // useEffect(() => {
  //   getAllSubjects().then((data) => {
  //     if (data.status) {
  //       setData(data.result);
  //     }
  //   });
  // }, []);

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
            </Route>
            <Route element={<PrivateRoute redirectPath={"/login"} />}>
              <Route path="profile" element={<Profile />} />
              <Route path="logout" element={<Logout />} />
            </Route>
            <Route path="login" element={<Login auth={false} />} />
            <Route path="auth" element={<Login auth={true} />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
          <Footer />
        </div>
      </BrowserRouter>
    </div>
  );
}
