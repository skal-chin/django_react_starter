import React, { useEffect, useState } from 'react';
import { HashRouter } from 'react-router-dom';
import { useRefreshToken } from './utils/use_refresh_token';
import { useApi } from './utils/use_api';
import { Router } from './components/router';

import './App.css';

import { AuthContext } from './utils/auth_context';
import { ApiContext } from './utils/api_context';

export const App = () => {
  const [accessToken, setAccessToken] = useState(null);
  const [loading, setLoading] = useState(true);

  const API_URL = process.env.REACT_APP_API_URL;
  useRefreshToken(accessToken, setAccessToken, API_URL);
  const api = useApi(accessToken, API_URL);
  
  const fetchToken = async () => {
    let headers = {
      'Content-Type': 'application/json',
    };

    const response = await fetch(`${API_URL}/sessions/`,
      {
        credentials: 'include',
        method: 'GET',
        headers: headers
    })
    .then(response => response.json());

    if (response.token) {
      setAccessToken(response.token);
    }
  };

  useEffect(() => {
    fetchToken();
    setLoading(false);

  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <AuthContext.Provider value={[accessToken, setAccessToken]}>
      <ApiContext.Provider value={api}>
        <HashRouter>
          <Router />
        </HashRouter>
      </ApiContext.Provider>
    </AuthContext.Provider>
  );
};