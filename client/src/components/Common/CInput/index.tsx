import React, {RefObject} from 'react';
import {classnames, TTailwindString} from '@@/tailwindcss-classnames';

interface Props {
    classes?: TTailwindString;
    type: string;
    label?: string;
	ref:RefObject<HTMLInputElement>;
    placeholder?: string;
    autofocus: boolean;
}

export const CInput = (props: Props): JSX.Element => {
	const classes = classnames('w-11/12', 'h-12', 'border', 'border-gray-400', 'rounded', 'm-2', 'p-5');
	const label = classnames('mx-2', 'mt-5');
	return (
		<div>
			{
				props.label ? <div className={label}>{props.label}</div> : null
			}
			<input type={props.type}
				ref={props.ref}
				placeholder={props.placeholder}
				autoFocus={props.autofocus}
				className={classnames(classes, props.classes)}/>
		</div>

	);
};

CInput.defaultProps = {
	type: 'text',
	autofocus: false,
};