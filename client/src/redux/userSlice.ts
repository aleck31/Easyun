import { createSlice } from '@reduxjs/toolkit';

export const userSlice = createSlice({
	name: 'user',
	initialState: {
		user: {
			name: 'xiaomo',
			age: 18,
		},
	},
	reducers: {},
});
export default userSlice.reducer;
