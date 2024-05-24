import axios from 'axios';
import toast from 'react-hot-toast';


export const $host = axios.create({
    baseURL: process.env.REACT_APP_SERVER_API,
    // baseURL: "http://192.168.124.128:8000/api/v1/",
})

export const $auth = axios.create({
    baseURL: process.env.REACT_AUTH_SERVER_API,
    // baseURL: "http://192.168.124.128/api/v1/authorization",
    withCredentials: true,
});

$auth.interceptors.response.use(
    response => response,
    error => {
        toast.error(error);
    });

$auth.interceptors.request.use((config) => {
    config.headers.Authorization = `Bearer ${localStorage.getItem('access_token')}`;
    return config;
})
