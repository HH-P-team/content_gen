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

export const postRefreshTokens = async (login, password) => {
	const { data } = await $auth({
		method: "POST",
		url: "/refresh",
		data: {
			login,
			password,
		},
	});

	return data;
};

export const postLogout = async () => {
	const { data } = await $auth({
		method: "POST",
		url: "/logout",
	});

	return data;
};

