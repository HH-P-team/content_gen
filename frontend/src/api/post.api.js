import { $host } from '.';

export const getAllPosts = async () => {
	const { data } = await $host.get('/posts');
	return data;
};

export default getAllPosts;