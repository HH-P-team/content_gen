import { $auth } from '..';

export const postRegistration = async (login, password) => {
	const { data } = await $auth({
		method: "POST",
		url: "/register",
		data: {
			login,
			password,
		},
	});
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
	return data;
};

export const postRefreshTokens = async (refresh_token) => {
	const { data } = await $auth({
		method: "POST",
		url: "/refresh",
		data: {
			refresh_token,
		},
	});

	return data;
};

export const postLogout = async (access_token) => {
	const { data } = await $auth({
		method: "POST",
		url: "/logout",
		data: {
			access_token,
		},
	});

	return data;
};

export const postCheck = async (access_token) => {
	const { data } = await $auth({
		method: "POST",
		url: "/check",
		data: {
			access_token,
		},
	});

	return data;
};

