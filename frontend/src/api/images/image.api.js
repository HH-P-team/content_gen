import { $host } from '..';

export const getImageByText = async (message) => {
	const { data } = await $host.post('/image/', {message});
	return data;
};

export const getImageBySubjectId = async (subjectID) => {
	const { data } = await $host.post(
		'/image/subject', 
		{subject_id: subjectID},
	);
	return data;
};

export const getImageByProductId = async (productID) => {
	const { data } = await $host.post(
		'/image/product', 
		{product_id: productID},
	);
	return data;
};

export const getImageByPostId = async (postID) => {
	const { data } = await $host.post(
		'/image/post', 
		{post_id: postID},
	);
	return data;
};

export default getImageByText

