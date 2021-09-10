import React, {useEffect, useState} from 'react';
import axios from 'axios';
import './App.css';
import {BrowserRouter as Router, Route, Link} from 'react-router-dom';
import {Switch} from 'react-router-dom';
import HomePage from './components/HomePage.js';
import SignInForm from './components/SignInForm.js';
import ResetPassword from './components/ResetPassword';

function App() {
  const lazyHomePage = React.lazy(() => import('./components/HomePage'));
  const lazyLogin = React.lazy(() => import('./components/SignInForm'));
  const lazyResetPassword = React.lazy(() => import('./components/ResetPassword'));
  return (
  <div>
    <Router>
      <React.Suspense fallback = {<div>Loading...</div>}>
        <Switch>
          <Route exact path = '/' component = {lazyHomePage}>
            
          </Route>

          <Route  path = '/login' component = {lazyLogin}/>

          <Route path = '/reset_password' component = {lazyResetPassword}/>

        </Switch>
      </React.Suspense>
    </Router>

  </div>
  );
}

export default App;
