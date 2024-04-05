import { useEffect } from "react";

export const useRefreshToken = (accessToken, setAccessToken, API_URL) => {

  useEffect(() =>{
    const options = {
      credentials : 'include',
      method : 'GET',
      headers: {
        'Content-Type': 'application/json',
      }
    };

    if (accessToken) {
      const interval = setInterval(async () => {
        const response = await fetch(`${API_URL}/sessions/`, options)
          .then(response => response.json());
        if (response.token) {
          setAccessToken(response.token);
        }
        else {
          clearInterval(interval);
          setAccessToken(null);
        }
      }, 1800000); // 30 minutes
    }
   }, [accessToken])
};