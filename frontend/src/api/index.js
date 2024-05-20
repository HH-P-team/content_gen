import axios from 'axios';

export const $host = axios.create({
    baseURL: process.env.REACT_APP_SERVER_API,
    // timeout: 1000,
    // headers: {'X-Custom-Header': 'foobar'}
})

export const $auth = axios.create({
    // baseURL: "/",
    // baseURL: process.env.REACT_AUTH_SERVER_API,
    // timeout: 1000,
    // headers: {'X-Custom-Header': 'foobar'}
});
