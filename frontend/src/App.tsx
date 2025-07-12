import React from 'react'
import Profile from './components/Profile';
import Menubar from './components/Menubar';
import { Route, Routes } from 'react-router-dom';
import Home from './components/Home';

function App() {
  return (
    <div style={{ backgroundColor: '#212121', height: '100vh', color: 'white' }}>
      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/profile" element={<Profile />} />
      </Routes>
    </div>
  )
}

export default App;