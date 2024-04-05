import { useRef } from 'react';

export const useApi = (accessToken, API_URL) => {
  const apiRef = useRef(new API());
  apiRef.current.accessToken = accessToken;
  apiRef.current.API_URL = API_URL;
  return apiRef.current;
};

export class API {
  accessToken = null;
  API_URL = null;

  get(url) {
    return fetch(`${this.API_URL}${url}`, {
      credentials: 'include',
      method: 'GET',
      headers: {
        Authorization : `Bearer ${this.accessToken}`,
        'Content-Type': 'application/json',
      },
    })
    .then(response => response.json());
  };

  post(url, data) {
    return fetch(`${this.API_URL}${url}`, {
      credentials: 'include',
      method: 'POST',
      headers: {
        Authorization : `Bearer ${this.accessToken}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json());
  };

  put(url, data) {
    return fetch(`${this.API_URL}${url}`, {
      credentials: 'include',
      method: 'PUT',
      headers: {
        Authorization : `Bearer ${this.accessToken}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json());
  };

  delete(url) {
    return fetch(`${this.API_URL}${url}`, {
      credentials: 'include',
      method: 'DELETE',
      headers: {
        Authorization : `Bearer ${this.accessToken}`,
        'Content-Type': 'application/json',
      },
    })
    .then(response => response.json());
  };
}