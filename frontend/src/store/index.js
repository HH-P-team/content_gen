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
		posts: [],
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

		case 'CASE_ADD_POSTS':
			return {
				...prevState,
				posts: [...value, ...prevState.posts],
			};

		case 'CASE_SET_POSTS':
			return {
				...prevState,
				posts: value,
			};

		case 'CASE_ADD_PRODUCT':
			const [ product ] = value;
			const { subject_id: subjectId} = product;
			const index = prevState.subjects.findIndex((el) => el.id === subjectId);
			return {
				...prevState,
				subjects: [
					...prevState.subjects.slice(0, index),
					{...prevState.subjects[index],
						products: [...prevState.subjects[index].products, product],
					}, 
					...prevState.subjects.slice(index + 1)
				]
				};

		default:
			return prevState;
	}
}

function updateSubject() {

}

export default configureStore({ reducer: mainReducer });