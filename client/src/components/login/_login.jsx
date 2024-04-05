import { useContext, useEffect, useState } from 'react';
import { useNavigate } from 'react-router';
import { ApiContext } from '../../utils/api_context';
import { AuthContext } from '../../utils/auth_context';

import { validateEmail } from '../../utils/validateEmail';
import { validatePassword } from '../../utils/validatePassword';

import '../../styles/common.css';

export const Login = () => {
  const LOGIN_URL = `${process.env.REACT_APP_API_URL}/login/`
  const api = useContext(ApiContext);
  const [, setAccessToken] = useContext(AuthContext);
  const navigate = useNavigate();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const [goodEmail, setGoodEmail] = useState(false);
  const [goodPassword, setGoodPassword] = useState(false);

  const signUp = () => {
    navigate('/signup');
  };

  const checkEmail = (e) => {
    setEmail(e);

    if (e === '') {
      return;
    }

    let emailStatus = validateEmail(e);
    setGoodEmail(emailStatus.valid);
  };

  const checkPassword = (p) => {
    setPassword(p);

    if (p === '') {
      return;
    }

    let passwordStatus = validatePassword(p);
    setGoodPassword(passwordStatus.valid);
  };

  const login = async () => {

    if (goodEmail && goodPassword) {

      const response = await fetch(LOGIN_URL, {
        credentials: 'include',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password })
      })
      
      if (response.status === 200) {
        const res = await response.json();
        setAccessToken(res.token);
        navigate('/');
      }

    }
  };

  return (
    <div>
      <div className='column box'>
        <h1>Login</h1>
        <div className='row'>
          <input
            className={`input ${goodEmail === false && email !== '' ? 'input-error' : ''}`}
            type='text'
            placeholder='Email'
            onChange={(e) => checkEmail(e.target.value)}  
          />
          <input 
            className={`input ${goodPassword === false && password !== '' ? 'input-error' : ''}`}
            type='password'
            placeholder='Password'
            onChange={(e) => checkPassword(e.target.value)}
          />
        </div>
        {(goodEmail === false && email !== '') && <p className='error-text'>Invalid email</p>}
        {(goodPassword === false && password !== '') && <p className='error-text'>Invalid password</p>}
        <div className='row'>
          <div 
            className='button'
            onClick={login}  
          >Login</div>
          <div 
            className='button'
            onClick={signUp}
          >Sign Up</div>

        </div>
      </div>
    </div>
  );

};