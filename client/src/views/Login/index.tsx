import { useTranslation } from 'react-i18next';

import React from 'react';
import { CButton } from '@/components/Common/CButton';
import { CInput } from '@/components/Common/CInput';
import { classnames } from '@@/tailwindcss-classnames';
import { Icon } from '@iconify/react';
import { useNavigate } from 'react-router-dom';


const LoginPage = (): JSX.Element => {
	const navigate = useNavigate();
	const login = (username: string, password: string) => {
		console.log(username, password);
		navigate('/home');
	};
	const {t, i18n} = useTranslation();
	const lang = i18n.language === 'ja' ? 'en' : 'ja';
	console.log(lang);
	const container = classnames('bg-gray-600', 'text-white', 'text-3xl', 'h-16', 'flex', 'items-center');

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
						<CInput
							placeholder={'Enter your username'}
							label={'Username *'}
						/>
						<CInput
							placeholder={'Enter your password'}
							type={'password'}
							label={'Password *'}
						/>

						<div className={classnames('flex', 'justify-center')}>
							<CButton
								classes={classnames('block', 'w-40', 'h-14', 'bg-yellow-650', 'text-white', 'font-bold', 'my-6')}
								click={() => {
									login('xiaomo', 'xiaomo123');
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