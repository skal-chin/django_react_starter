import { useContext, useEffect, useState } from "react";
import { ApiContext } from "../../utils/api_context";
import { AuthContext } from "../../utils/auth_context";

export const Home = () => {

  const api = useContext(ApiContext);
  const [accessToken, setAccessToken] = useContext(AuthContext);
  const [user, setUser] = useState({});
  const [loading, setLoading] = useState(true);

  const getMe = async () => {
    const me = await api.get('/me/');
    setUser(me);
  };

  useEffect(() => {
    if (!accessToken) {
      return;
    }

    getMe();
    setLoading(false);
  }, []);

  const logout = async () => {
    await api.get('/logout/');
    setAccessToken(null);
  }

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
        </div>
      </div>
    </div>
  );
};