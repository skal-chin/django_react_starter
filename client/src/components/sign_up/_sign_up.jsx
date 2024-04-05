import { useContext, useState, useEffect } from 'react';
import { useNavigate } from 'react-router';
import { ApiContext } from '../../utils/api_context';
import { AuthContext } from '../../utils/auth_context';

import { validateEmail } from '../../utils/validateEmail';
import { validatePassword } from '../../utils/validatePassword';

import '../../styles/common.css';

export const SignUp = () => {
  const api = useContext(ApiContext);
  const [, setAccessToken] = useContext(AuthContext);
  const navigate = useNavigate();

  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const [goodUsername, setGoodUsername] = useState(false);
  const [goodEmail, setGoodEmail] = useState(false);
  const [goodPassword, setGoodPassword] = useState(false);

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

  const signUp = async () => {

    if (goodEmail && goodPassword) {

      let response = await api.post('/signup/', { username, email, password })
        .then(response => response.json());

      if (response.token) {
        setAccessToken(response.token);
        navigate('/');
      } 
      else {
        console.log('Sign up failed');
      }
    }
  };

  if (loading) {
    return (
      <div>
        <h1>Loading...</h1>
      </div>
    );
  }

  return (
    <div>
      <div className='column box'>
        <h1>Sign Up</h1>
        <input
          className={`input ${goodUsername === false ? 'input-error' : ''}`}
          type='text'
          placeholder='username'
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          className={`input ${goodEmail === false ? 'input-error' : ''}`}
          type="text" 
          placeholder="email" 
          onChange={e => checkEmail(e.target.value)}
        />
        <input 
          className={`${goodPassword === false ? 'input input-error' : 'input'}`}
          type="new-password" 
          placeholder="password" 
          onChange={e => checkPassword(e.target.value)}
        />
        {goodUsername === false ? <div className='error-text'>Invalid username</div> : null}
        {goodEmail === false ? <div className='error-text'>Invalid email</div> : null}
        {goodPassword === false ? <div className='error-text'>Invalid password</div> : null}
        <div
          className='button' 
          onClick={signUp}
          >Sign Up
        </div>
      </div>
    </div>
  );

};