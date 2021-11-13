import { configureStore } from '@reduxjs/toolkit';
import personReducer from '@/redux/userSlice';

const store = configureStore({
	reducer: {
		person: personReducer,
	},
});

export default store;
