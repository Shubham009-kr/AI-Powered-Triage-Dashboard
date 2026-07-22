import { create } from "zustand";

import api from "../api/api";
import type { Message } from "../types/message";

interface MessageStore {
  messages: Message[];
  selectedMessage: Message | null;

  loading: boolean;

  fetchMessages: () => Promise<void>;

  selectMessage: (message: Message) => void;
}

export const useMessageStore = create<MessageStore>((set) => ({
  messages: [],

  selectedMessage: null,

  loading: false,

  fetchMessages: async () => {
    set({ loading: true });

    try {
        const response = await api.get<Message[]>("/messages");

        set({
        messages: response.data,
        });
    } catch (error) {
        console.error("Failed to fetch messages:", error);
    } finally {
        set({
        loading: false,
        });
    } 
  },

  selectMessage: (message) =>
    set({
      selectedMessage: message,
    }),
}));