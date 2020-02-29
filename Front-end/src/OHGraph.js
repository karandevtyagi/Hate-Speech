import React from 'react';
import Plot from 'react-plotly.js';

class OHGraph extends React.Component {
  render() {
    return (
      <Plot
        data={[
          {
            x: [1, 2, 3],
            y: [2, 6, 3],
            type: 'scatter',
            mode: 'lines+points',
            marker: {color: 'red'},
          },
          {type: 'bar', x: [1, 2, 3], y: [2, 5, 3]},
        ]}
        layout={ {width: 320, height: 240, title: 'A Fancy Plot'} }
      />
    );
  }
}

export OHGraph;

/*
html, body {
  width: 100%;
  height: 100%;
}
*/

/*

/*
import Api from './Api';


export default {
  send(credentials) {
    return Api().post('/', username);
  },
  retrieve() {
    return Api().get('/user', details);
  },
};


import axios from 'axios';

export default () => axios.create({
  baseURL: 'http://localhost:3000/',
});

*/
