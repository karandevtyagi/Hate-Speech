import React from 'react';
import { Link } from 'react-router-dom'
import Plot from 'react-plotly.js';
import fetch from './fetchData.js'

import icon from './icon.png';
import avatar from './avatar.png';

class User extends React.Component {

  /*
  POST Method
  username
  GET method
  Name
  Handle
  Image url
  O score
  H score
  N score
  Most used words array
  object
  Resize image in css
  */

  constructor(props) {
    super(props);
    this.state = {
      name: '',
      handle: '',
      image_url: '',
      o_score: '',
      h_score: '',
      n_score: '',
      word_array: [],
      hate_tweets:[],
      offensive: []
    }
  }

  componentDidMount() {
    let handle = localStorage.getItem('user');
    console.log(handle);
    const fetchData = async () => {
      const response = await fetch.fetch(handle);
      this.setState({
        name: response.data.username,
        handle: response.data.userscreenanme,
        image_url: response.data.userimage,
        o_score: response.data.result.o,
        h_score: response.data.result.h,
        n_score: response.data.result.c,
        word_array: response.data.result.word.slice(10),
        hate_tweets:response.data.result.hate,
        hscore:response.data.result.hscore,
        offensive: response.data.result.offensive
      })
    }
    fetchData();
  }

  /* Add function to set state for above values */

  render() {
    return (
      <div className="App">
        <nav className="twit-analyser">
          <img alt="" src={icon} className="icon"/>
          OH-Score
        </nav>
        <div className="content">
                      <img alt="avatar" src={this.state.image_url} className="avatar"/>
          <div className="text">@{this.state.handle}</div>
          <p>{this.state.name}</p>
            <div>
              <p className="head">Numeric Statistics</p>
              <p>Number of hate tweets: {this.state.h_score}</p>
              <p>Number of offensive tweets: {this.state.o_score}</p>
              <p>Number of neither tweets: {this.state.n_score}</p>
              <p>H-Score: {this.state.hscore}</p>
            </div>
            <div>
              <p className="head">Graphical Visualisation</p>
                <Plot
                  data={[
                    {
                      type: 'scatter',
                      mode: 'lines+points',
                      marker: {color: 'red'},
                    },
                    {type: 'bar', x: ["Hate", "Offensive", "Neither"], y: [this.state.h_score,this.state.o_score, this.state.n_score]},
                  ]}
                  layout={ {width: 500, height: 500, title: 'Tweet type'} }
                />
            </div>
            <p>
            {this.state.hate_tweets.join("\n\n")}
            </p>            
            <p>
            {this.state.hate_tweets.join("\n\n")}
            </p>
            <p>
            {this.state.offensive.join("\n\n")}
            </p>
            <Link to="/">
              <button className="go-back">Go Back?</button>
            </Link>
          </div>
      </div>
    );
  }

}

export default User;