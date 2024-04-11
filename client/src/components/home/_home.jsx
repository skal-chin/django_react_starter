import { useContext, useEffect, useState } from "react";
import { ApiContext } from "../../utils/api_context";
import { AuthContext } from "../../utils/auth_context";

export const Home = () => {

  const api = useContext(ApiContext);
  const [accessToken, setAccessToken] = useContext(AuthContext);
  const [user, setUser] = useState({});
  const [loading, setLoading] = useState(true);
  const [myClicks, setMyClicks] = useState([]);

  const getMe = async () => {
    const me = await api.get('/me/');
    setUser(me);
  };

  const getClicks = async () => {
    const clicks = await api.get(`/get-clicks/${user.id}/`);
    setMyClicks(clicks.clicks);
  };

  useEffect(() => {
    if (!accessToken) {
      return;
    }

    getMe();
    setLoading(false);
  }, []);

  useEffect(() => {
    if (Object.keys(user).length === 0) {
      return;
    }

    getClicks();

  }, [user])

  const logout = async () => {
    await api.get('/logout/');
    setAccessToken(null);
  }

  const postClick = async () => {
    const response = await api.post('/click/', {'user_id': user.id});
    setMyClicks([...myClicks, response]);
  };


  if (loading) {
    return <div>Loading...</div>;
  }
  
  return (
    <div>
      <div className='column box'>
        <h1>Home</h1>
        <p>Welcome to the home page, {user.username}</p>
        <div className='row'>
          <button
            className='button' 
            onClick={logout}
          >Logout</button>
          <button
            className='button' 
            onClick={postClick}
          >Click</button>
        </div>

        <h2>My Clicks</h2>

        {myClicks.length === 0 && <p>No clicks yet</p>}
        <ul>
          {myClicks && myClicks.map(click => (
            <li key={click.id}>{`${click.id} at ${click.clicked_at}`}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};