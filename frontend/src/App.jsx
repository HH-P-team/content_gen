import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './Components/App/Header/Header';
import Footer from './Components/App/Footer/Footer';
import Sidebar from './Components/App/Sidebar/Sidebar';
import Subjects from './Components/Pages/Subjects';
import Products from './Components/Pages/Products';
import Posts from './Components/Pages/Posts';
import { useState, useEffect } from 'react';
import getAllSubjects from './api/subjects/subject.api'

export default function App() {

  const [data, setData] = useState([]);

  useEffect(() => {
    getAllSubjects().then((data) => {
      if (data.status) {
        setData(data.result);
      }
    });
  }, []);

  return (
    <div className="App">
      <BrowserRouter>
      <Sidebar />
        <div className='Wrapper'>
          <Header />
            <Routes>
              <Route path='*' element={<Subjects data={data}/>}></Route>
              <Route path='products' element={<Products data={data}/>}></Route>
              <Route path='posts' element={<Posts />}></Route>
            </Routes>
        <Footer />
        </div>
        </BrowserRouter>
    </div>
  );
}
