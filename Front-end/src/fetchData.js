import Api from './api.js';

export default {
  fetch(handle) {
    return Api().post('user', {username: handle})
  }
};
