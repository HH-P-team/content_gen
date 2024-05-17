import { createBrowserRouter } from 'react-router-dom';
import App from '../App';
import adminRouter from './admin.router';
// import methodistRouter from './methodist.router';
// import trainerRouter from './trainer.router';
// import checkInRouter from './check.in.router';

export default function createRouter(role) {
	return createBrowserRouter([
		{
			path: '/',
			element: <App sidebar />,
			loader: () => {
				return null;
			}, // loader to fetch data before render
			children:
				(role === 'admin' && adminRouter)
		},
		// {
		// 	path: '/',
		// 	element: <App />,
		// 	children: checkInRouter
		// }
	]);
}
