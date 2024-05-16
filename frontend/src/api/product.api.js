import { $host } from '.';

export const getAllProducts = async () => {
	const { data } = await $host.get('/products');
	return data;
};