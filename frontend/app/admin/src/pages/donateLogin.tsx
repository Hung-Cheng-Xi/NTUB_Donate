import React from 'react';

const LoginPage: React.FC = () => {
  const googleAuthParams = {
    client_id: '452962124993-i7tb7ic5b4e0ei05c6v6hplkb64huqjn.apps.googleusercontent.com',
    redirect_uri: 'http://donate.ntub.edu.tw:8001/admin/',
    response_type: 'code',
    scope: 'email',
  };

  const handleGoogleSignIn = () => {
    const baseUrl = 'https://accounts.google.com/o/oauth2/v2/auth';
    const queryParams = new URLSearchParams(googleAuthParams).toString();
    window.location.href = `${baseUrl}?${queryParams}`;
  };

  return (
    <div
      className="flex items-center justify-center min-h-screen bg-blue-100 bg-cover bg-center"
      style={{
        backgroundImage: `url('https://s3-alpha-sig.figma.com/img/90ac/40b7/8e7f07c3515688a250b9503246027cf5?Expires=1728864000&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=jk~2Jds~r1YSHCiwEUmRifm5-t6qtxzNJWKxseHjZXSEwkqgevqrgQ3MLT6dnkGamDx3iwSrMHrZbqh90FGSgCd54wUMzE9s7GWRpj2cx7hYNioIOu5K5mIqLn~bIloR9wxR~-30RfnztGm15sHlxi972WPaOy-Y3O5Q2lnUeGBlQgxoZJnXoxiz76nWgKM3SLbjnFZUr72JE~XejSLTbwuwJoK9n-Sfhx05ma9pAEplKxbuiO4k-x09WP7Dbh3GCtu8wu~dwsIsHQH~GeGt~nJge-zgTebP1Q18pjPdWR8ydp5k54nosKMW5jXcxJzAWRlL2w1JU9zXCb~odtST9w__')`,
      }}
    >
      <div className="w-full max-w-md p-8 space-y-6 bg-white rounded-md shadow-md">
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
