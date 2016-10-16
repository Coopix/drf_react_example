import 'babel-polyfill';

import React from 'react';
import { render } from 'react-dom';
import { AppContainer } from 'react-hot-loader';
import App from './app';

const target = document.getElementById('content');
const node = (
  <AppContainer>
    <App />
  </AppContainer>
);

render(node, target);

if (module.hot) {
  module.hot.accept('./app', () => {
    const NextApp = require('./app').default;
    render(<AppContainer><NextApp /></AppContainer>, target);
  })
}
