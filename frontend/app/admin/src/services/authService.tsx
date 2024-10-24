import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

// 使用 Google 登入
export const loginWithGoogle = async (code: string) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/admin/auth/login/`, {
      code,
    });
    const accessToken = response.data.access_token;

    // 存储 token (可以使用 localStorage 或其他方式)
    localStorage.setItem('access_token', accessToken);

    return accessToken;
  } catch (error) {
    console.error('Failed to get access token', error);
    throw error; // 抛出错误，让调用者处理
  }
};

// 利用 refresh token 來刷新 access token
export const refreshAccessToken = async () => {
  try {
    const response = await axios.post(
      `${API_BASE_URL}/api/admin/auth/refresh/`,
      {},
      {
        withCredentials: true, // 允許發送 cookies
      },
    );
    return response.data;
  } catch (error) {
    console.error('Failed to refresh access token', error);
    throw error;
  }
};
