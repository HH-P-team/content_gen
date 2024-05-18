import { $host } from '..';

const getAllProducts = async () => {
	const { data } = await $host.get('/products');
	return data;
};

export const getProductByText = async (message) => {
	const { data } = await $host.post('/products', {message});
	return data;
};

export default getAllProducts;

