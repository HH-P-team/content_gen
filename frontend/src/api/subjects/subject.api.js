import { $host } from '..';

const getAllSubjects = async () => {
	const { data } = await $host.get('/subjects');
	return data;
};

export default getAllSubjects;