import React, { useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { loginWithGoogle } from '../services/authService';

const LoginPage: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const googleAuthParams = {
    client_id:
      '452962124993-i7tb7ic5b4e0ei05c6v6hplkb64huqjn.apps.googleusercontent.com',
    // redirect_uri: 'http://donate.ntub.edu.tw:8001/admin/',
    redirect_uri: 'http://localhost:5173/admin/login/',
    response_type: 'code',
    scope: 'email',
  };

  const handleGoogleSignIn = () => {
    const baseUrl = 'https://accounts.google.com/o/oauth2/v2/auth';
    const queryParams = new URLSearchParams(googleAuthParams).toString();
    window.location.href = `${baseUrl}?${queryParams}`;
  };

  useEffect(() => {
    const queryParams = new URLSearchParams(location.search);
    const code = queryParams.get('code');

    if (code) {
      loginWithGoogle(code)
        .then(() => {
          navigate('/admin/');
        })
        .catch((error) => {
          console.error('Failed to login with Google', error);
        });
    }
  }, [location, navigate]);

  return (
    <div className="flex items-center justify-center min-h-screen bg-blue-white bg-cover bg-center">
      <div className="w-full max-w-md p-8 space-y-6 bg-white rounded-md shadow-md border">
        <img
          src={'http://i.imgur.com/YJjEvK8.gif'}
          alt="NTUB Logo"
          className="mx-auto h-16 w-16"
        />
        <h2 className="text-3xl font-bold text-center text-gray-800">
          Sign in
        </h2>
        <div className="mt-8">
          <button
            onClick={handleGoogleSignIn}
            className="flex items-center justify-center w-full px-4 py-2 space-x-2 font-semibold text-gray-700 bg-white border rounded-md hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <svg
              className="w-6 h-6"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 48 48"
            >
              <path
                fill="#4285F4"
                d="M24 9.5c3.9 0 7 1.6 9.1 4.2l6.8-6.8C35.6 2.7 30.1 0 24 0 14.8 0 6.8 5.9 2.8 14.3l7.9 6.1C12.5 12.3 17.7 9.5 24 9.5z"
              />
              <path
                fill="#34A853"
                d="M46.9 24.5c0-1.6-.1-3.1-.4-4.5H24v9.1h13.2c-.6 3.3-2.5 6.1-5.4 7.9l8.4 6.5c4.9-4.5 7.7-11.1 7.7-18.9z"
              />
              <path
                fill="#FBBC05"
                d="M11.8 28.4c-1-2.5-1.5-5.2-1.5-8s.5-5.5 1.5-8L2.8 5.7C1 9.3 0 13.5 0 18c0 4.5 1 8.7 2.8 12.3l9-7.9z"
              />
              <path
                fill="#EA4335"
                d="M24 48c6.5 0 11.9-2.1 15.8-5.8l-8.4-6.5c-2.4 1.6-5.4 2.5-8.5 2.5-6.7 0-12.3-4.5-14.3-10.7l-9 7.9C6.8 42.1 14.8 48 24 48z"
              />
            </svg>
            <span>Sign in with Google</span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
