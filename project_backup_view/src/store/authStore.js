import { create } from 'zustand';
import { persist } from 'zustand/middleware';

const useAuthStore = create(
  persist(
    (set) => ({
      accessToken: null,
      refreshToken: null,
      user: null,

      login: (tokens, userData) => set ({
        accessToken: tokens.access,
        refreshToken: tokens.refresh,
        user: userData,
      }),
      logout: () => set({
        accessToken: null,
        refreshToken: null,
        user: null
      }),

      setTokens: (tokens) => set({
        accessToken: tokens.access,
        refreshToken: tokens.refresh
      })
    }),
    {
      name: 'auth-storage',
    }
  )
);

export default useAuthStore;