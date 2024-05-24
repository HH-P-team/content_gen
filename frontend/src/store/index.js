import { configureStore } from '@reduxjs/toolkit';
// import Cookie from 'js-cookie';

// const mainReducer = (
// 	prevState = {
// 		user: {
// 			role: Cookie.get('role') || 'admin'
// 		}
// 	},
// 	action
// ) => {
// 	const { type, payload } = action;

// 	switch (type) {
// 		case 'SET_ROLE':
// 			Cookie.set('role', payload);
// 			return {
// 				...prevState,
// 				user: {
// 					...prevState.user,
// 					role: payload
// 				}
// 			};
// 		default:
// 			return prevState;


const mainReducer = (
	prevState = {
		activeElementId: 0,
		addSubjectMenuState: false,
		addProductMenuState: false,
		addPostMenuState: false,
		subjects: [],
		// products: {},
		// posts: {},
	},
	action
) => {
	const { type, value } = action;

	switch (type) {
		case 'CASE_SET_ACTIVE_ELEMENT_ID':
			return {
				...prevState,
				activeElementId: value,
			};

		case 'CASE_SUBJECT_MENUSTATE':
			return {
				...prevState,
				addSubjectMenuState: value,
			};

		case 'CASE_PRODUCT_MENUSTATE':
			return {
				...prevState,
				addProductMenuState: value,
			};

		case 'CASE_POST_MENUSTATE':
			return {
				...prevState,
				addPostMenuState: value,
			};

		case 'CASE_ADD_SUBJECTS':
			return {
				...prevState,
				subjects: [...value, ...prevState.subjects],
			};

		case 'CASE_SET_SUBJECTS':
			return {
				...prevState,
				subjects: value,	
			};

		case 'CASE_ADD_PRODUCT':
			const [ product ] = value;
			const { subject_id: subjectId} = product;
			console.log(subjectId);
			console.log(prevState.subjects);
			console.log(value);
			const index = prevState.subjects.findIndex((el) => el.id === subjectId);
			console.log(index);
			// const updatedSubject = prevState.subjects.filter((subject) => subject.id === subjectId)[0]
			return {
				...prevState,
				subjects: [
					...prevState.subjects.filter((subject) => subject.id !== subjectId), 
					...prevState.subjects.filter((subject) => subject.id === subjectId)
				]
				};

		default:
			return prevState;
	}
}

function updateSubject() {

}

export default configureStore({ reducer: mainReducer });