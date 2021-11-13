import React from 'react';
import { CPartialLoading } from '@/components/Common/CPartialLoading/CPartialLoading';
import { TTailwindString } from '@@/tailwindcss-classnames';

export interface ContainerProps {
	loading: boolean;
	classes?: TTailwindString;
	component: JSX.Element;

}

export const CContainer = (props: ContainerProps): JSX.Element => {
	return props.loading ? <CPartialLoading classes={props.classes}/> : props.component;
};