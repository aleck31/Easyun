import React from 'react';
import { classnames, TTailwindString } from '@@/tailwindcss-classnames';

interface Props {
	classes?: TTailwindString;
}

export const CHeader = (props: Props): JSX.Element => {
	const container = classnames('bg-gray-600','text-white','h-12','flex','items-center');
	const content = classnames('ml-6');
	return (
		<div className={container}>
			<span className={content}>Easyun</span>
		</div>
	);
};
