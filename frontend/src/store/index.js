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
// 	}
// };

// export default configureStore({ reducer: mainReducer });

const mainReducer = (
	prevState = {
		buttonState: 1,
		buttonState1: 2,
		addSubjectMenuState: false,
		subjects: [],
		products: {},
		posts: {},
	},
	action
) => {
	const { type, value } = action;

	switch (type) {
		case 'CASE_SUBJECT_MENUSTATE':
			return {
				...prevState,
				addSubjectMenuState: value,
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
			var { subjectId, product} = value;

			const prevProduct = prevState.products[subjectId] ? prevState.products[subjectId] : []

			return {
				...prevState,
				products: {
					...prevState.products,
					...{[subjectId]: [...prevProduct, ...[product]]},
				}
			};
	
		case 'CASE_SET_PRODUCTS':
			var { subjectId, product} = value;
			
			return {
				...prevState,
				products: {
					...prevState.products,
					...{[subjectId]: product},
				}
			};

		default:
			return prevState;
	}
}

export default configureStore({ reducer: mainReducer });