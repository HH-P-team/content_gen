import './index.css';
import React, { useMemo } from 'react';
import ReactDOM from 'react-dom/client';
import { Provider, useSelector } from 'react-redux';
import { RouterProvider } from 'react-router-dom';
import reportWebVitals from './reportWebVitals';
import store from './store';
import createRouter from './routes';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Provider store={store}>
      <Root />
    </Provider>
  </React.StrictMode>
);

function Root() {
	const role = useSelector((state) => state.user.role);
	const router = useMemo(() => {
		return createRouter(role);
	}, [role]);
	return <RouterProvider router={router} />;
}

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
