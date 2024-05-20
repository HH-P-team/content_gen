import { $auth } from '..';
import Cookies from 'js-cookie';

export const postRegistration = async (login, password) => {
	const { data } = await $auth({
		method: "POST",
		url: "/register",
		data: {
			login,
			password,
		},
	});

	// if (cookie.get(CSRF_TOKEN_COOKIE_KEY) && data.username) {
	//   setUser(response.data);
	// }

	return data;
};



export const postAuthenticate = async (login, password) => {
	const { data } = await $auth({
		method: "POST",
		url: "/authenticate",
		data: {
			login,
			password,
		},
	});

	if (Cookies.get("access_token") && Cookies.get("refresh_token") && data.login) {
		// setUser(data);
	}

	return data;
};


export const postRefreshTokens = async (login, password) => {
	const { data } = await $auth({
		method: "POST",
		url: "/refresh",
		data: {
			login,
			password,
		},
	});

	if (Cookies.get("CSRF_TOKEN_COOKIE_KEY") && data.login) {
		// setUser(data);
	}

	return data;
};



export const postLogout = async () => {
	const { data } = await $auth({
		method: "POST",
		url: "/logout",
		// data: {
		// 	login,
		// 	password,
		// },
	});

	// if (cookie.get(CSRF_TOKEN_COOKIE_KEY) && data.login) {
	// 	setUser(data);
	// }

	return data;
};

