import React, { Suspense } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Navigate, Routes } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from '@/redux/store';
import '@/assets/styles/index.css';

import '@/i18n';
import { CFullLoading } from '@/components/Common/CFullLoading';
import { Route } from 'react-router';
import NotFound from '@/views/NotFound';
import Home from '@/views/Home';
import DataCenter from '@/views/DataCenter';
import Resource from '@/views/Resource';
import AddServer from '@/views/Resource/AddServer';
import AddBucket from '@/views/Resource/Storage/AddBucket';
import AddDisk from '@/views/Resource/Storage/AddDisk/insex';
import LoginPage from '@/views/Login';
import Account from '@/views/Account';


const App = (): JSX.Element => {
	return (
		<Suspense fallback={<CFullLoading/>}>
			<Routes>
				<Route path="/" element={<LoginPage/>}/>
				<Route path="home" element={<Home/>}/>
				<Route path="dataCenter" element={<DataCenter/>}/>
				<Route path="resource">
					<Route index element={<Resource/>}/>
					<Route path="addServer" element={<AddServer/>}/>
					<Route path="addBucket" element={<AddBucket/>}/>
					<Route path="addDisk" element={<AddDisk/>}/>
				</Route>
				<Route path="login" element={<LoginPage/>}/>
				<Route path="404" element={<NotFound/>}/>
				{/* <Route
					path="*"
					element={<Navigate to="/"/>}/> */}
				<Route path='account' element={<Account/>}/>
			</Routes>
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
