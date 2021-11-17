import { useTranslation } from 'react-i18next';

import React from 'react';
import { RouteComponentProps } from 'react-router-dom';
import { CButton } from '@/components/Common/CButton';
import { CInput } from '@/components/Common/CInput';
import { CHeader } from '@/components/Logic/CHeader';
import { classnames } from '@@/tailwindcss-classnames';

interface Props {
	history: RouteComponentProps['history'];
	location: RouteComponentProps['location'];
	match: RouteComponentProps['match'];
}

const LoginPage = (props: Props): JSX.Element => {

	const login = (username: string, password: string) => {
		console.log(username, password);
		props.history.push('/home');
	};
	const {t, i18n} = useTranslation();
	// const lang = i18n.language === 'ja' ? 'en' : 'ja';


	return (
		<div>
			<CHeader/>
			<div
				className={classnames('flex', 'justify-center', 'items-center', 'w-full', 'h-full','mt-36')}>
				<div id="login-container"
					 className={classnames('w-3/12', 'border', 'p-8')}>
					<div id="login-content">
						<div id="login-title" className={classnames('m-2','mb-5','font-bold','text-lg')}>
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

						<div className={classnames('flex','justify-center')}>
							<CButton
								classes={classnames('block', 'w-40', 'h-14', 'bg-yellow-650', 'text-white','font-bold', 'my-6')}
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