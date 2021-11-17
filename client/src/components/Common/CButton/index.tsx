import React from 'react';
import {classnames, TTailwindString} from '@@/tailwindcss-classnames';

export interface CButtonProps {
    children;
    classes?: TTailwindString;
    click?: () => void;
}

export const CButton = (props: CButtonProps): JSX.Element => {
	return <button
		onClick={props.click}
		className={classnames(props.classes)}>
		{props.children}
	</button>;
};