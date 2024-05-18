import { $host } from '..';

export const getImageByText = async (message) => {
	const { data } = await $host.post('/image/', {message});
	return data;
};

export default getImageByText