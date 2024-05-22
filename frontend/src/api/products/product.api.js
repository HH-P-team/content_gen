import { $host } from '..';

const getProducts = async (subjectId) => {
	const { data } = await $host.get(
		'/products', 
		{params: {
			subject_id: subjectId,
		}
	});
	return data;
};

export const getProductByText = async (message) => {
	const { data } = await $host.post('/products', {message});
	return data;
};

export const getProductsBySubjectId = async (subjectId) => {
	const { data } = await $host.post('/products', {subjectId});
	return data;
}

export const createProduct = async (subjectId) => {
	console.log('createProduct');
	const { data } = await $host.post(
		'/products', 
		{subject_id: subjectId},
	);
	return data;
}

export default getProducts;

