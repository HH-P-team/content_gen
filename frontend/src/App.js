import logo from './lightplus_bg_x2.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import getAllSubjects from './api/subject.api';
import Header from './components/app/header/Header';
import Footer from './components/app/footer/Footer';
import Container from './components/app/container/Container';
import Sidebar from './components/app/sidebar/Sidebar';

function App() {

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
      <Sidebar />
      <div className='Wrapper'>
        <Header />
        <Container data={data}/>
        <Footer />
      </div>
    </div>
  );
}

export default App;
