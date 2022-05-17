import React from 'react';
import { Link } from 'react-router-dom'
import icon from './icon.png';
import avatar from './avatar.png';

class Home extends React.Component {

  constructor(props) {
    super(props);
    this.state = { query: '' }
    this.setHandle = this.setHandle.bind(this)
  }

  /* On click of button set query to field value*/
  setHandle() {
    let handle = document.querySelector(".enter-handle").value;
    this.setState({query: handle});
    localStorage.removeItem('user');
    localStorage.setItem('user', handle);
  }

  render() {
    /* Add fade in animations for navbar, content and user icon */
    return (
      <div className="App">
        <nav className="twit-analyser">
          <img alt="" src={icon} className="icon"/>
          OH-Score
        </nav>
        <div className="content">
          <img alt="avatar" src={avatar} className="avatar"/>
          <div className="text">Enter your chosen handle name to check OH-Score!</div>
          <div className="field">
            <input placeholder="Handlename" className="enter-handle" type="text"/>
            <Link to="/user">
              <button className="go" onClick={this.setHandle}>Go!</button>
            </Link>
          </div>
        </div>
      </div>
    );
  }
}

export default Home;
