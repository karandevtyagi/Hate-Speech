import React from 'react';
import './App.css';

// Import react-router-dom
import { Route } from 'react-router-dom'
import Home from './Home';
import User from './User';
import axios from 'axios';

class App extends React.Component {

  render() {
  	axios.defaults.headers.post['Content-Type'] ='application/x-www-form-urlencoded';
    return (
      <div>
        <Route exact path="/" component={ Home } />
        <Route exact path="/user" component={ User } />
      </div>
    );
  }
}

export default App;
