import { useContext } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { AuthContext } from '../utils/auth_context';

import { Home } from './home/_home';
import { Login } from './login/_login';
import { SignUp } from './sign_up/_sign_up';

export const Router = () => {
  const [accessToken] = useContext(AuthContext);

  return (
    <Routes>
      <Route path="/" element={accessToken ? <Home /> : <Navigate replace to="/login" />} />
      <Route path="/login" element={!accessToken ?  <Login /> : <Navigate replace to="/" />} />
      <Route path="/signup" element={<SignUp />} />
    </Routes>
  );
}