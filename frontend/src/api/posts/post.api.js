import { $host } from '..';

export const getAllPosts = async () => {
	const { data } = await $host.get('/posts');
	return data;
};

export const createPost = async (productId, text) => {
	const { data } = await $host.post(
		'/posts',
		{
			product_id: productId,
			prompt: text,
		}
	);
	return data;
}

export default getAllPosts;
