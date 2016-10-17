import fetch from 'isomorphic-fetch';

function fetchHandler(index, params) {
  function checkStatus(response) {
    if (response.status >= 200 && response.status < 300) {
      return response;
    } else {
      const error = new Error(response.statusText);
      error.response = response;
      throw error;
    }
  }

  function parseJSON(response) {
    return response.json();
  }

  function fetchHandler(url, service, method) {
    service = service || '';
    const endpoint = url + service;
    method = method || 'GET';
    const options = {
      method,
    };
    console.log('Attempting', method, method === 'GET' ? 'from' : 'to', endpoint);
    startTime = new Date();

    return fetch(endpoint, options)
      .then(checkStatus)
      .then(parseJSON)
      .then(function(json) {
        return json;
      }).catch(function(error) {
        console.log(
          `Request failed! ${error.response.statusText} (${error.response.status})`
        );
      })
  }
  return fetchHandler(index, params);
}

export default fetchHandler;
