import { $host } from '..';

const getAllSubjects = async () => {
	const { data } = await $host.get('/subjects/');
	return data;
};

export const createSubject = async (subjectName) => {
	const { data } = await $host.post(
		'/subjects', 
		{subject_name: subjectName},
	);
	return data;
}

export default getAllSubjects;