import React, { lazy, Suspense } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Redirect, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from '@/redux/store';
import '@/assets/styles/index.css';

import '@/i18n';
import { CFullLoading } from '@/components/Common/CFullLoading';
import { Route } from 'react-router';
import NotFound from '@/views/NotFound';

const Home = lazy(() => import('@/views/Home'));
const Login = lazy(() => import('@/views/Login'));
const DataCenter = lazy(() => import('@/views/DataCenter'));


const App = (): JSX.Element => {
	return (
		<Suspense fallback={<CFullLoading/>}>
			<Switch>
				<Route path="/" component={Login} exact/>
				<Route path="/home" component={Home}/>
				<Route path="/dataCenter" component={DataCenter}/>
				<Route path="/login" component={Login}/>
				<Route path="/404" component={NotFound}/>
				<Redirect to="/404"/>
			</Switch>
		</Suspense>
	);
};


ReactDOM.render(
	<React.StrictMode>
		<BrowserRouter>
			<Provider store={store}>
				<App/>
			</Provider>
		</BrowserRouter>
	</React.StrictMode>,
	document.getElementById('root')
);
