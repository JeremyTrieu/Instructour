import React, {useEffect, useState} from 'react';
import axios from 'axios';
import './HomePage.css';
function HomePage() {
  
  return (
    <div className="bodyBackground">
        <div className = "logoArea">
          <a href = '/' className = "logo"><img src = {'../instructour_logo.png'}/></a>
        </div>
        <div className = "info">
          <div className = "searchArea">
          <input className = "searchBox" type = "text" placeholder = "Type your instructor's name..." />
        </div>
        </div>  
        <div className = "loginArea">
          <a href="/login" className = "login_button_home">Or log in to write instructor reviews</a>
        </div>
    </div>
  );
}

export default HomePage;
