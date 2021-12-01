import {useTranslation} from 'react-i18next';

import React, {createRef} from 'react';
import {CButton} from '@/components/Common/CButton';
import {classnames} from '@@/tailwindcss-classnames';
import {Icon} from '@iconify/react';
import {useNavigate} from 'react-router-dom';

import userService from '@/service/userService';

interface LoginRes {
    token: string,
}

const LoginPage = (): JSX.Element => {
	const navigate = useNavigate();
	const usernameRef = createRef<HTMLInputElement>();
	const passwordRef = createRef<HTMLInputElement>();
	const login = async (username?: string, password?: string) => {
		if (!username || !password) {
			return;
		}
		console.log(username, password);
		const res = await userService.login<LoginRes>(username, password);
		console.log(res.token);
		navigate('/home');
	};


	const {t, i18n} = useTranslation();
	const lang = i18n.language === 'ja' ? 'en' : 'ja';
	console.log(lang);
	const container = classnames('bg-gray-600', 'text-white', 'text-3xl', 'h-16', 'flex', 'items-center');
	const classes = classnames('w-9/12', 'h-12', 'border', 'border-gray-400', 'rounded', 'mx-2', 'my-10', 'p-5');
	return (
		<div>
			<div id="header" className={container}>
				<div className={classnames('ml-10', 'flex-grow')}>
					<div>
                        Easyun
						<span className={classnames('float-right', 'mr-40', 'cursor-pointer')}>
							<Icon className={classnames('ml-10', 'inline-block')} icon="ant-design:setting-filled"
								color="#5c6f9a" width="25" height="25"
								hFlip={true} fr={undefined}/>
							<Icon className={classnames('ml-3', 'inline-block')} icon="iconoir:nav-arrow-down"
								color="#5c6f9a" width="25" height="25"
								hFlip={true} fr={undefined}/>
						</span>
					</div>
				</div>
			</div>
			<div
				className={classnames('flex', 'justify-center', 'items-center', 'w-full', 'h-full', 'mt-36')}>
				<div id="login-container"
					className={classnames('w-4/12', 'border', 'p-8')}>
					<div id="login-content">
						<div id="login-title" className={classnames('m-2', 'mb-5', 'font-bold', 'text-lg')}>
							{t('Login')}
						</div>

						<input type='text'
							ref={usernameRef}
							placeholder='Enter your username'
							className={classnames(classes)}/>

						<input type='password'
							ref={passwordRef}
							placeholder='Enter your password'
							className={classnames(classes)}/>


						<div className={classnames('flex', 'justify-center')}>
							<CButton
								classes={classnames('block', 'w-40', 'h-14', 'bg-yellow-650', 'text-white', 'font-bold', 'my-6')}
								click={() => {
									login(usernameRef.current?.value, passwordRef.current?.value);
								}}
							>
                                Login
							</CButton>
						</div>
						{/*<CButton click={() => i18n.changeLanguage(lang)}>*/}
						{/*	{`change to ${lang}`}*/}
						{/*</CButton>*/}
					</div>
				</div>
			</div>
		</div>
	);
};

export default LoginPage;