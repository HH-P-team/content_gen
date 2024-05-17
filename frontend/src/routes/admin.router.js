import App from "../App";

const adminRouter = [
	{
		path: '/',
		element: <App />
	},
	{
		path: '/products',
		element: <App />,
		local: 'Продукты'
	},
];

export default adminRouter;
